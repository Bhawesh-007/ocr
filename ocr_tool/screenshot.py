"""Screen region capture, backed by KDE's `spectacle` CLI.

Spectacle owns the interactive rectangle-selection overlay; this module
only shells out to it, waits for it to finish, and locates the result.
"""

import subprocess
from pathlib import Path

from config import SCREENSHOTS_DIR


class ScreenshotCancelledError(Exception):
    """Raised when the user cancels region selection (e.g. presses Escape)."""


def capture_region(filename: str) -> Path:
    """Prompt the user to drag-select a screen region and save it as PNG.

    Args:
        filename: Name to save as, with or without a .png extension.
            Only the basename is used, so stray "/" in the input can't
            redirect the save outside SCREENSHOTS_DIR.

    Returns:
        Path to the saved screenshot file.

    Raises:
        ScreenshotCancelledError: the user cancelled the selection.
        RuntimeError: spectacle exited with an unexpected error.
    """
    stem = Path(filename).name.removesuffix(".png")
    output_path = SCREENSHOTS_DIR / f"{stem}.png"

    result = subprocess.run(
        ["spectacle", "-b", "-n", "-r", "-o", str(output_path)],
        capture_output=True,
        text=True,
    )

    if not output_path.exists():
        raise ScreenshotCancelledError(
            "No screenshot was saved — selection was likely cancelled."
        )

    if result.returncode != 0:
        raise RuntimeError(
            f"spectacle exited with code {result.returncode}: {result.stderr.strip()}"
        )

    return output_path


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python screenshot.py <filename>")
        sys.exit(1)

    try:
        saved_path = capture_region(sys.argv[1])
    except ScreenshotCancelledError as exc:
        print(exc)
    else:
        print(f"Saved screenshot to {saved_path}")
