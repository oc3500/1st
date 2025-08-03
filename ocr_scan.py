from PIL import Image
import pytesseract
import sys


def ocr_image(path: str) -> str:
    """Return text detected in the image at ``path``.

    The OCR engine is configured for simplified Chinese and English so that
    Chinese characters, Latin letters and digits are recognised.
    """
    img = Image.open(path)
    # chi_sim is the language pack for simplified Chinese in tesseract
    return pytesseract.image_to_string(img, lang="chi_sim+eng")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python ocr_scan.py <image_path>")
        sys.exit(1)
    path = sys.argv[1]
    text = ocr_image(path)
    print(text)


if __name__ == "__main__":
    main()
