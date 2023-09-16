import re

import requests

from config.settings import (ADMIN_BASE_URL, ADMIN_LOGIN_URL, ADMIN_PASSWORD,
                             ADMIN_USERNAME)

session = requests.Session()

data = {
    "username": ADMIN_USERNAME,
    "password": ADMIN_PASSWORD,
}

response = session.post(ADMIN_LOGIN_URL, data=data)
match = re.search(r'token=([A-Za-z0-9]+)', response.url)
token = match.group(1)

params = {
    "token": token
}
product_data = {
    "product_description[1][name]": "test_api_python",
    "model": "1234141"
}
session.post(f"{ADMIN_BASE_URL}catalog/product/add", params=params, data=product_data)
