import re
from typing import Tuple

from requests import Session

from config.settings import ADMIN_LOGIN_URL, ADMIN_PASSWORD, ADMIN_USERNAME

__all__ = ("get_token",)


def get_token() -> Tuple[str, Session]:
    session = Session()
    data: dict = {
        "username": ADMIN_USERNAME,
        "password": ADMIN_PASSWORD,
    }
    response = session.post(ADMIN_LOGIN_URL, data=data)
    match = re.search(r"token=([A-Za-z0-9]+)", response.url)
    token = match.group(1)

    return token, session
