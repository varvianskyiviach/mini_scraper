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
    if match is not None:
        token = match.group(1)
    else:
        raise Exception("Token has not received. Please check you login or password")

    return token, session
