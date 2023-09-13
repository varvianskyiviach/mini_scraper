import os
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
STATIC_ROOT = ROOT_DIR / "staticfiles"
STATIC_ROOT_IMAGES = STATIC_ROOT / "images"

MAIN_URL = "https://wizkids.com/upm"

FTP_HOST = os.getenv("FTP_HOST")
FTP_USERNAME = os.getenv("FTP_USERNAME")
FTP_PASSWORD = os.getenv("FTP_PASSWORD")
