import os
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).parent.parent
STATIC_ROOT = ROOT_DIR / "staticfiles"

FILE_EXEL_NAME = "list_new.csv"
load_dotenv(dotenv_path=f"{ROOT_DIR}/.env")

# ====================
# parser configuration
# ====================
# url
URL_MAPPING: dict = {"wizkids": "https://wizkids.com/upm", "dom_igor": "https://domigr.com.ua/ua/c-modelirovanie/c-miniatures/critical-role/"}

# ====================
# web app cofiguration
# ====================

# --------------------
# url
# - local development -
ADMIN_BASE_URL = "http://localhost:8080/admin/index.php?route="
# - production -
# ADMIN_BASE_URL = "https://lisgames.com.ua/admin/index.php?route="
ADMIN_LOGIN_URL = f"{ADMIN_BASE_URL}common/login"
# endpoints
ADMIN_FILE_UPLOAD = "common/filemanager/upload"
ADMIN_PRODUCT_ADD = "catalog/product/add"
# --------------------

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

DIR_CATALOG = 'catalog'
DIR_FOTO = 'fotki'
DIR_PROJECT = "wizkids"
