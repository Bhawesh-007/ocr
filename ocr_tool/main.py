"""Entry point: capture a screen region, then OCR it.

Chains screenshot.capture_region() and ocr.extract_text() so the two
stay independently testable while this gives you the one command you
actually run.
"""

from ocr import extract_text
from screenshot import ScreenshotCancelledError, capture_region


def _prompt_name() -> str:
    while True:
        name = input("Save as: ").strip()
        if name:
            return name
        print("Name can't be empty.")


def main() -> None:
    name = _prompt_name()

    try:
        screenshot_path = capture_region(name)
    except ScreenshotCancelledError as exc:
        print(exc)
        return

    print(f"Saved screenshot to {screenshot_path}")

    run_ocr = input("Run OCR? [y/N]: ").strip().lower() == "y"
    if run_ocr:
        text_path = extract_text(screenshot_path)
        print(f"Saved text to {text_path}")


if __name__ == "__main__":
    main()
