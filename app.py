import os
import io
import joblib
import pytesseract
from PIL import Image
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

# Initialize FastAPI
app = FastAPI(
    title='Document Intelligence API',
    description='OCR, Classification, and Extraction',
    version='1.0.0'
)

# Load models 
# Note: Ensure these files exist in your directory. 
# Use 'vectorizer.pkl' if the file is in the same folder as this script.
try:
    vectorizer = joblib.load('vectorizer.pkl')
    classifier = joblib.load('classifier.pkl')
    print("Models loaded successfully.")
except FileNotFoundError:
    print("Error: Model files not found. Ensure you ran the training code first.")

@app.get('/')
def root():
    return {
        'message': 'Document Intelligence API',
        'version': '1.0.0',
        'endpoints': ['/classify', '/extract', '/process']
    }
