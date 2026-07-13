"""Text extraction from screenshots, backed by Tesseract via pytesseract.

pytesseract doesn't do OCR itself — it hands the image to the local
`tesseract` binary and parses its output. Pillow is what turns the
PNG file on disk into the in-memory Image object tesseract needs.
"""

from pathlib import Path

import pytesseract
from PIL import Image

from config import SCREENSHOT_TEXT_DIR, TESSERACT_LANG


def extract_text(screenshot_path: Path) -> Path:
    """Run OCR on a screenshot and save the result as a sibling .txt file.

    Args:
        screenshot_path: PNG produced by screenshot.capture_region().

    Returns:
        Path to the saved .txt file.
    """
    image = Image.open(screenshot_path)
    text = pytesseract.image_to_string(image, lang=TESSERACT_LANG)

    text_path = SCREENSHOT_TEXT_DIR / f"{screenshot_path.stem}.txt"
    text_path.write_text(text)

    return text_path


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python ocr.py <screenshot_path>")
        sys.exit(1)

    saved_path = extract_text(Path(sys.argv[1]))
    print(f"Saved text to {saved_path}")
