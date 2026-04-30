import os
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Adjust path if needed, but wait, maybe it's not installed or not in PATH

artifact_dir = r"C:\Users\Asus\.gemini\antigravity\brain\79bd0899-6a81-4421-ba35-e14ea338268a"
images = [
    "media__1777453841845.png",
    "media__1777453915341.png",
    "media__1777453931029.png",
    "media__1777453938031.png",
    "media__1777461807691.png",
    "media__1777461814952.jpg"
]

try:
    for img_name in images:
        img_path = os.path.join(artifact_dir, img_name)
        if os.path.exists(img_path):
            img = Image.open(img_path)
            text = pytesseract.image_to_string(img)
            print(f"--- {img_name} ---")
            print(text.strip())
            print("-" * 20)
        else:
            print(f"File not found: {img_path}")
except Exception as e:
    print(f"Error: {e}")
