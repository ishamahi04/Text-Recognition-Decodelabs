"""
Project 4: Image or Text Recognition (Basic)
Intern        : Isha Khatri
Company       : DecodeLabs
Track         : Optional Mastery Phase - Image/Text Recognition (Basic)

WHAT THIS SCRIPT DOES (in simple words):
1. It opens an image that has some text written/printed on it.
2. It cleans up the image a little bit so the text is easier to read
   (this is called "pre-processing").
3. It uses a ready-made library called "pytesseract" (this is just a
   Python wrapper for Google's free Tesseract OCR engine) to read the
   text inside the image.
4. It prints the text on the screen and also saves it to a .txt file.
5. It also tells us how "confident" the model is about the text it found.

NOTE FOR A BEGINNER:
We are NOT training our own AI model here. We are simply USING a
pre-trained model (Tesseract) that already knows how to read text from
images. This is called "Model Implementation", not "Model Training".
"""

import cv2                 # OpenCV - used only for basic image cleaning
import pytesseract         # The OCR (Optical Character Recognition) library
import os

# pytesseract internally calls the tesseract program installed on the
# system. On most systems this line is not even required, but it is
# kept here so the script also works on Windows where the path must be
# set manually. Uncomment and edit the line below if needed:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def load_image(image_path):
    """Step 1: Simply read the image from the disk using OpenCV."""
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Could not find/open the image at: {image_path}")

    return image


def preprocess_image(image):
    """
    Step 2: Basic pre-processing.
    Real-world images (photos, scans) are often noisy, tilted or have
    bad lighting. Two very simple, beginner-friendly steps help the OCR
    engine read text more accurately:
        a) Convert the image to grayscale (black & white) - color does
           not help an OCR engine, it just adds extra noise.
        b) Apply a simple threshold - this turns the image into pure
           black-and-white (binary), which makes the letters stand out
           clearly from the background.
    """
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Simple binary threshold (anything above 150 becomes white,
    # everything else becomes black). 150 is a beginner-friendly,
    # easy-to-tune number for clean, well-lit images.
    _, processed_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)

    return processed_image


def extract_text(processed_image):
    """Step 3: Run the pre-trained Tesseract OCR model on the image."""
    extracted_text = pytesseract.image_to_string(processed_image)
    return extracted_text


def get_confidence_scores(processed_image):
    """
    Bonus Step: Tesseract can also tell us how confident it is about
    each word it detected (0 = not confident at all, 100 = fully
    confident). We use this to show that we understand model output,
    not just raw text.
    """
    data = pytesseract.image_to_data(processed_image, output_type=pytesseract.Output.DICT)

    confidences = []
    for word, conf in zip(data["text"], data["conf"]):
        word = word.strip()
        conf = int(conf)
        if word != "" and conf > 0:
            confidences.append((word, conf))

    return confidences


def save_output(text, output_path):
    """Step 4: Save the extracted text to a simple .txt file."""
    with open(output_path, "w") as f:
        f.write(text)


def main():
    # ---- Basic settings (beginner style: simple variables, no classes) ----
    input_image_path = "sample_images/sample_text.png"
    output_text_path = "output/extracted_text.txt"

    print("=" * 50)
    print(" DecodeLabs - Project 4: Basic Text Recognition")
    print("=" * 50)

    # Step 1: Load image
    print(f"\n[1/4] Loading image from: {input_image_path}")
    image = load_image(input_image_path)

    # Step 2: Pre-process image
    print("[2/4] Pre-processing image (grayscale + threshold)...")
    processed_image = preprocess_image(image)

    # Step 3: Extract text using the pre-trained OCR model
    print("[3/4] Running pre-trained OCR model (pytesseract)...")
    extracted_text = extract_text(processed_image)

    # Step 4: Display the output clearly
    print("[4/4] Done! Here is what the model read from the image:\n")
    print("-" * 50)
    print(extracted_text.strip())
    print("-" * 50)

    # Bonus: show confidence scores so we prove we understand model output
    print("\nWord-by-word confidence scores (model output interpretation):")
    confidences = get_confidence_scores(processed_image)
    for word, conf in confidences:
        print(f"  -> '{word}'  -  Confidence: {conf}%")

    # Save results to a file as well
    os.makedirs("output", exist_ok=True)
    save_output(extracted_text, output_text_path)
    print(f"\nExtracted text also saved to: {output_text_path}")


if __name__ == "__main__":
    main()
