import os
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).parent.parent
STATIC_ROOT = ROOT_DIR / "staticfiles"
STATIC_ROOT_IMAGES = STATIC_ROOT / "images"

load_dotenv(dotenv_path=f'{ROOT_DIR}/.env')

# ====================
# parser configuration
# ====================
MAIN_URL = "https://wizkids.com/upm"

# ====================
# web app cofiguration
# ====================
# --------------------
# local development
ADMIN_BASE_URL = "http://localhost:8080/admin/index.php?route="
# production
# ADMIN_BASE_URL = "https://lisgames.com.ua/admin/index.php?route="
# --------------------
ADMIN_LOGIN_URL = f'{ADMIN_BASE_URL}common/login'
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")


FTP_HOST = os.getenv("FTP_HOST")
FTP_USERNAME = os.getenv("FTP_USERNAME")
FTP_PASSWORD = os.getenv("FTP_PASSWORD")
