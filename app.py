import os
import io
import re
import joblib
import spacy
import pytesseract
from PIL import Image
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

# 1. Initialize FastAPI

app = FastAPI(
    title="Document Intelligence System",
    description="Upload documents for OCR and NLP extraction",
    version="1.0"
)


# 2. Load Models & NLP
# Make sure classifier.pkl and vectorizer.pkl are in the same folder as this file
try:
    classifier = joblib.load('classifier.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
    nlp = spacy.load('en_core_web_sm')
    print("✅ Models and NLP loaded successfully")
except Exception as e:
    print(f"❌ Error loading dependencies: {e}")

# 3. Extraction Logic (From Week 7)
def extract_dates(text):
    patterns = [r'\d{1,2}/\d{1,2}/\d{4}', r'\d{4}-\d{2}-\d{2}']
    return re.findall('|'.join(patterns), text)

def extract_amounts(text):
    return re.findall(r'\$?\d{1,3}(?:,\d{3})*(?:\.\d{2})?', text)

def extract_entities(text):
    doc = nlp(text)
    return {
        "organizations": [ent.text for ent in doc.ents if ent.label_ == "ORG"],
        "locations": [ent.text for ent in doc.ents if ent.label_ in ["GPE", "LOC"]]
    }

# 4. Endpoints
@app.get('/')
def root():
    return {"status": "online", "message": "Document Intelligence API is running"}

@app.post('/process')
async def process_document(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert('RGB')
        
        # OCR
        text = pytesseract.image_to_string(image)
        
        # Classification
        vec = vectorizer.transform([text])
        prediction = classifier.predict(vec)[0]
        confidence = max(classifier.predict_proba(vec)[0])
        
        return {
            "document_type": str(prediction),
            "confidence": round(float(confidence), 2),
            "extracted_data": {
                "dates": extract_dates(text),
                "amounts": extract_amounts(text),
                "entities": extract_entities(text)
            }
        }
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# Note: In Codespaces, we run this from the terminal, not inside the script.
