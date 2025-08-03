# 1st

This repository contains an example script for running OCR on a JPEG image to
extract Chinese characters, English text and digits.

## Usage

1. Install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) with the
   language packages for English (`eng`) and simplified Chinese (`chi_sim`).
   Make sure the `tesseract` command is available on your system.

2. Install the Python dependencies:

   ```bash
   pip install pillow pytesseract
   ```

3. Run the script with an image path:

   ```bash
   python ocr_scan.py example.jpg
   ```

The script will print the text recognised in the image.
