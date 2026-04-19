# OCR Receipt Processing Project

## 1. Project Overview
This project focuses on building and evaluating an OCR (Optical Character Recognition) pipeline for extracting text from receipt images. The workflow includes image preprocessing, text extraction using multiple OCR engines, and performance comparison between methods.



## 2. Objectives
- To extract text from real-world receipt images using OCR techniques  
- To improve OCR accuracy through image preprocessing  
- To compare Tesseract OCR and EasyOCR performance  
- To evaluate the effect of preprocessing on OCR output quality  



## 3. Dataset Description
- Dataset Used :/kaggle/input/datasets/trainingdatapro/ocr-receipts-text-detection
- Receipt images (clean, blurry, and noisy samples)  
- Formats include JPG images (evaluated from 0 to 4 jpg images)  
- Data sourced from Kaggle / custom dataset  



## 4. Image Preprocessing Pipeline

### 4.1 Grayscale Conversion
- Converted RGB images to grayscale  
- Reduced computational complexity  

### 4.2 Noise Reduction
- Applied Gaussian blur to reduce image noise  
- Improved text clarity for OCR models  

### 4.3 Thresholding Techniques
- Binary thresholding (fixed threshold)  
- Adaptive Gaussian thresholding (handles lighting variations)  

### 4.4 Purpose of Preprocessing
- Enhance text visibility  
- Reduce background noise  
- Improve OCR accuracy  



## 5. OCR Methods Used

### 5.1 Tesseract OCR
- Traditional rule-based OCR engine  
- Works best on clean and structured text  
- Requires preprocessing for optimal results  

### 5.2 EasyOCR
- Deep learning-based OCR model  
- More robust to noise and distortion  
- Performs better on real-world images  



## 6. Implementation Workflow

### Step 1: Image Loading
- Loaded images using OpenCV  

### Step 2: Preprocessing
- Applied grayscale, denoising, and thresholding  

### Step 3: OCR Extraction
- Extracted text using Tesseract  
- Extracted text using EasyOCR  

### Step 4: Comparison
- Compared outputs based on character length  
- Evaluated confidence scores (EasyOCR)  



## 7. Key Experiments

### Experiment 1: Original vs Preprocessed Image
- OCR performed on raw image  
- OCR performed on enhanced image  
- Observed improvement in readability  

### Experiment 2: OCR Engine Comparison
- Tesseract vs EasyOCR outputs compared  
- EasyOCR performed better on noisy images  



## 8. Observations
- Preprocessing significantly improves OCR accuracy  
- Adaptive thresholding works better under uneven lighting  
- EasyOCR is more robust for real-world receipts  
- Tesseract performs better on clean images  



## 9. Challenges Faced
- Poor image quality (blur and noise)  
- Inconsistent OCR outputs  
- Execution order issues in notebook environment  
- Variable dependency errors (e.g., undefined variables)  



## 10. Learning Outcomes

### 10.1 Image Processing Skills
- Grayscale conversion  
- Noise reduction techniques  
- Thresholding methods  

### 10.2 OCR Understanding
- Difference between rule-based and deep learning OCR  
- Impact of preprocessing on OCR accuracy  

### 10.3 Programming Skills
- Debugging runtime errors in notebooks  
- Writing modular functions  
- Managing pipeline execution order  

### 10.4 Analytical Skills
- Comparing model outputs critically  
- Evaluating OCR confidence vs text length  
- Understanding trade-offs between OCR systems  



## 11. Conclusion
The project demonstrates that OCR performance is highly dependent on image preprocessing and model selection. A combination of Tesseract and EasyOCR, along with proper preprocessing, leads to significantly improved text extraction from receipt images.
