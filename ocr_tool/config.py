"""Central location for filesystem paths and shared constants.

Other modules import from here instead of hardcoding paths, so the
output directories only have to be defined once.
"""

from pathlib import Path

# Anchored to this file's location on disk, not the process's working
# directory, so paths stay correct no matter where the script is launched from.
PROJECT_ROOT: Path = Path(__file__).resolve().parent

# Extracted OCR text is saved outside the project, in the user's own
# ~/OCR directory, rather than inside the repo. Screenshots and text
# each get their own subfolder so the two file types don't mix.
OCR_ROOT: Path = Path.home() / "OCR"
SCREENSHOTS_DIR: Path = OCR_ROOT / "screenshots"
SCREENSHOT_TEXT_DIR: Path = OCR_ROOT / "screenshot_text"

# Ensure output directories exist as soon as config is imported, so
# downstream modules can write into them without checking first.
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
SCREENSHOT_TEXT_DIR.mkdir(parents=True, exist_ok=True)

# Tesseract OCR language (ISO 639-2 code as used by the tessdata files).
TESSERACT_LANG: str = "eng"
