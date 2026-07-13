#!/bin/bash
# Launched by the Ctrl+Alt+O KDE shortcut. Opens a terminal that stays
# alive after main.py exits, so you can read the printed paths (or any
# error) before it closes.
cd "$(dirname "$0")"
konsole --hold -e /home/tron007/projects/screenshot_text/.venv/bin/python main.py