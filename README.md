# 🧾 OCR Receipt Processing & Digit Recognition System

## 1. Project Overview
This project presents a complete pipeline for **OCR-based receipt text extraction** combined with **image preprocessing** and **deep learning-based digit recognition**.

The system integrates:
- Classical OCR techniques (Tesseract, EasyOCR)
- Advanced image preprocessing (deskewing, perspective correction)
- Morphological image operations
- CNN-based handwritten digit classification (MNIST)
- Extracts text from real-world receipt images using OCR (Tesseract & EasyOCR).
- Deploys a FastAPI interface to serve machine learning models


## 2. Objectives

- Extract text from real-world receipt images using OCR  
- Improve OCR accuracy through preprocessing techniques  
- Compare Tesseract OCR and EasyOCR performance  
- Implement perspective correction and automatic deskewing  
- Demonstrate morphological image operations  
- Build and train a CNN model for digit recognition  
- Visualize training performance and predictions
- Deploy the system as a **FastAPI REST API application**  
- Enable real-time image upload and processing 



## 3. Dataset Description

### OCR Dataset
- Source: Kaggle OCR Receipts Dataset  
- Contains:
  - Clean images  
  - Blurry images  
  - Noisy samples  
- Format: JPG images  

### Digit Classification Dataset
- MNIST Handwritten Digits Dataset  
- 28×28 grayscale images  
- 10 classes (digits 0–9)

### Companies Dataset
- Contains 4 classes
  --invoice
  --receipts
  --memos
  --forms


## 4. Image Preprocessing Pipeline

### 4.1 Grayscale Conversion
- Converts RGB images to grayscale  
- Reduces computational complexity  

### 4.2 Noise Reduction
- Gaussian Blur applied  
- Improves OCR readability  

### 4.3 Thresholding Techniques
- Binary Thresholding  
- Adaptive Gaussian Thresholding  

### 4.4 Perspective Correction
- Corrects distorted or tilted receipt images  
- Ensures proper alignment  

### 4.5 Automatic Deskewing
- Detects skew angle using image geometry  
- Rotates image to horizontal alignment  

### 4.6 Morphological Operations
- **Erosion** → Removes noise  
- **Dilation** → Expands features  
- **Opening** → Removes small noise  
- **Closing** → Fills gaps  

### 4.7 Purpose of Preprocessing
- Enhance text visibility  
- Reduce noise and distortion  
- Improve OCR accuracy  



## 5. OCR Methods Used

### 5.1 Tesseract OCR
- Rule-based OCR engine  
- Performs well on clean text  
- Sensitive to noise  

### 5.2 EasyOCR
- Deep learning-based OCR  
- Robust to noise and distortions  
- Better for real-world images  



## 6. CNN Model for Digit Recognition

### Architecture
- Input: 28×28 grayscale images  
- Convolutional layers (feature extraction)  
- ReLU activation  
- MaxPooling layers  
- Flatten layer  
- Dense layers  
- Output layer: Softmax (10 classes)  

### Training Details
- Optimizer: Adam  
- Loss Function: Categorical Crossentropy  
- Batch Size: 128  
- Epochs: 10  
- Validation Split: 0.1  

### Results
- Achieved **~99% test accuracy** on MNIST  
- Demonstrated strong generalization  

## 7. FastAPI Backend & System Deployment

### 7.1 FastAPI Overview
The system is deployed using **FastAPI**, enabling real-time interaction with OCR and digit recognition models through REST APIs.

FastAPI provides:
- High-performance asynchronous API handling  
- Automatic Swagger UI documentation  
- Easy integration with ML/DL models  
- Lightweight deployment  

---

### 7.2 Main Application Structure

```bash
app.py
```
## 8. Implementation Workflow

1. **Image Loading**
   - Load receipt images using OpenCV  

2. **Preprocessing**
   - Grayscale → Denoising → Thresholding  
   - Perspective correction  
   - Deskewing  
   - Morphological processing  

3. **OCR Extraction**
   - Extract text using Tesseract  
   - Extract text using EasyOCR  

4. **Digit Classification**
   - Feed processed images into CNN  
   - Predict digit classes  

5. **Evaluation**
   - Compare OCR outputs  
   - Analyze performance  
   - Evaluate CNN accuracy

6. **FastAPI Deployment**
   - Wrap OCR and CNN pipeline into REST API endpoints  
   - Enable real-time image upload and processing  
   - Return structured JSON responses  
   - Provide Swagger UI (`/docs`) for testing APIs  
   - Deploy application using Uvicorn server (`uvicorn app:app --reload`)



## 9. Key Experiments

### Experiment 1: Original vs Preprocessed Images
- OCR applied on raw images  
- OCR applied on enhanced images  
- Significant improvement observed  

### Experiment 2: OCR Engine Comparison
- Tesseract vs EasyOCR  
- EasyOCR performs better on noisy data  

### Experiment 3: CNN Performance
- Training vs validation accuracy plotted  
- Model convergence verified  

### Experiment 3: Trained LogisticRegression Model 
- classifier determines if a document is an *Invoice, Receipt, Memo or Contract*.
- Achieved 83.3% accuracy
- created vectorizer and classifier for deployment


## 9. Visualizations

- Training History (Accuracy vs Epochs)  
- Loss vs Epochs  
- Training vs Test Accuracy Comparison  
- Sample Predictions Visualization  



## 10. Observations

- Preprocessing significantly improves OCR accuracy  
- Adaptive thresholding handles lighting variations effectively  
- Deskewing and perspective correction improve alignment  
- EasyOCR performs better on noisy receipts  
- CNN achieves high accuracy on digit recognition  



## 11. Challenges Faced

- Poor image quality (blur, noise)  
- OCR inconsistencies  
- Notebook execution order issues  
- Dependency and variable errors  
- Handling real-world distortions  



## 12. Learning Outcomes

### Image Processing
- Advanced preprocessing techniques  
- Morphological operations  
- Geometric corrections  

### OCR Systems
- Rule-based vs deep learning OCR  
- Impact of preprocessing  

### Deep Learning
- CNN architecture design  
- Model training and evaluation  
- Performance visualization  

### Programming Skills
- Debugging pipelines  
- Modular code design  
- Workflow management  

### Analytical Skills
- Model comparison  
- Performance evaluation  
- Error analysis  



## 13. Key Achievements

- ✔ Perspective correction implemented  
- ✔ Automatic deskewing achieved  
- ✔ Morphological operations demonstrated  
- ✔ OCR pipeline using Tesseract & EasyOCR  
- ✔ CNN model successfully built  
- ✔ Achieved ~99% accuracy on MNIST  
- ✔ Training history visualized  
- ✔ Predictions verified
- ✔ Fast API (Application) Deployment



## 14. Future Improvements

- Extend to full OCR system (structured data extraction)  
- Integrate advanced models (CNN + LSTM / Transformers)  
- Deploy as web or mobile application  
- Improve robustness under extreme noise conditions  



## 15. Requirements

```txt
fastapi
uvicorn
python-multipart
pytesseract
spacy
scikit-learn
tensorflow
joblib
opencv-python
pillow
numpy
```

## API Access & Endpoints
**server execution: uvicorn app:app --host 0.0.0.0 --port 8000 --reload**

**Base URL: https://roseanne-harsh-jacob.ngrok-free.dev**

**Interactive UI: Append /docs to the URL to access Swagger UI.**

## 👩‍💻 Author

**Ayesha Ameer (shaheenaameer2003@gmail.com)**  
Physics & Electronics | AI | Computer Vision | NLP  


