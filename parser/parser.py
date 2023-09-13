from typing import List

import requests
from bs4 import BeautifulSoup

from config.settings import MAIN_URL
from miniatures.models import UncommitedMiniatures


def parse_mode() -> List[UncommitedMiniatures]:

    session = requests.Session()
    responce = session.get(MAIN_URL)

    html_content = responce.text

    soup = BeautifulSoup(html_content, "html.parser")
    table = soup.find("table", class_="tablepress-id-108")
    results_table = table.find("tbody", class_="row-hover").find_all("tr")

    all_web_miniatures: list[UncommitedMiniatures] = []

    for row in results_table:
        columns = row.find_all("td")
        try:
            sku = int(columns[0].get_text())
        except Exception:
            try:
                sku = int(columns[1].get_text())
            except Exception:
                sku = None
        try:
            image = columns[3].img['src']
        except Exception:
            image = None

        name = columns[2].get_text()

        if sku is not None:
            all_web_miniatures.append(UncommitedMiniatures(
                sku=sku, name=name, image=image))

    return all_web_miniatures
