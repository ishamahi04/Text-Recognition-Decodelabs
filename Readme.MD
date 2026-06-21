# Project 4 - Image/Text Recognition (Basic)
**DecodeLabs Internship | Artificial Intelligence Track | Batch 2026**

## 📌 About This Project
This is my 4th and final project for the DecodeLabs AI Internship.
The goal of this project (Optional Mastery Phase) is to implement a
**basic text recognition (OCR)** tool using a pre-trained library —
**not** to build or train a new AI model from scratch.

In simple words: the script takes an image that has text in it, and
uses a ready-made OCR engine (Tesseract) to "read" that text and print
it out, along with how confident the model is about each word.

## 🎯 Goal
Implement a basic image/text recognition task using available
libraries, perform recognition on a sample input, and display the
output clearly.

## 🧰 Tools & Libraries Used
| Library | Purpose |
|---|---|
| `opencv-python` (cv2) | Reading the image and basic pre-processing (grayscale + thresholding) |
| `pytesseract` | Python wrapper for Google's Tesseract OCR engine — does the actual text recognition |
| Tesseract OCR (system package) | The actual pre-trained OCR engine used under the hood |

## 📂 Project Structure
```
project4-text-recognition/
│
├── text_recognition.py        # Main script (run this)
├── requirements.txt           # Python libraries needed
├── sample_images/
│   └── sample_text.png        # Sample input image with text
├── output/
│   └── extracted_text.txt     # Text extracted by the script (created after running)
└── README.md                  # This file
```

## ⚙️ How It Works (Step by Step)
1. **Load Image** – The script reads the sample image using OpenCV.
2. **Pre-process Image** – Converts the image to grayscale and applies
   a simple black & white threshold so the text stands out clearly.
3. **Recognize Text** – Passes the cleaned image to `pytesseract`,
   which uses the pre-trained Tesseract OCR model to detect and read
   the text.
4. **Display Output** – Prints the extracted text to the console along
   with a confidence score (%) for each word, and saves the text to
   `output/extracted_text.txt`.

## ▶️ How to Run This Project

### 1. Install Tesseract OCR engine (one-time system setup)
- **Windows:** Download and install from
  https://github.com/UB-Mannheim/tesseract/wiki
- **Mac:** `brew install tesseract`
- **Linux:** `sudo apt install tesseract-ocr`

### 2. Install Python libraries
```bash
pip install -r requirements.txt
```

### 3. Run the script
```bash
python text_recognition.py
```

### 4. Check the output
- The recognized text will be printed on the screen.
- It will also be saved inside `output/extracted_text.txt`.

## 🖼️ Sample Input
A simple image containing the text:
```
Hello DecodeLabs!
Project 4 - OCR Test 2026
Basic Text Recognition Demo
```

## ✅ Sample Output
```
Hello DecodeLabs!
Project 4 - OCR Test 2026
Basic Text Recognition Demo

Word-by-word confidence scores:
  -> 'Hello'        - Confidence: 93%
  -> 'DecodeLabs!'  - Confidence: 92%
  -> 'Project'      - Confidence: 96%
  -> 'OCR'          - Confidence: 96%
  -> 'Recognition'  - Confidence: 95%
  ...
```

## 📚 What I Learned (Key Skills)
- How to use a **pre-trained AI library** (Tesseract OCR) instead of
  training a model from zero.
- Basic **image pre-processing** using OpenCV (grayscale, thresholding).
- How to **read and interpret model output**, including confidence
  scores.
- Writing clean, simple, beginner-friendly Python code with clear
  comments and step-by-step structure.

## 🙅 Dos and Don'ts I Followed
**Dos:**
- ✅ Used a pre-trained/ready-made library (pytesseract) as required.
- ✅ Kept the code simple and beginner-level (plain functions, no
  advanced classes/design patterns).
- ✅ Added clear comments explaining every step.
- ✅ Displayed the output clearly in the console and saved it to a file.

**Don'ts:**
- ❌ Did not train a custom deep learning model from scratch.
- ❌ Did not use advanced/complex techniques (no custom CNNs, no
  unnecessary abstraction or design patterns).
- ❌ Did not hardcode the extracted text — it is genuinely detected by
  the OCR engine from the image.

## 🙋 Author
**Intern, AI Track – DecodeLabs (Batch 2026)**
Project 4 of 4 — Internship Completed 🎉
