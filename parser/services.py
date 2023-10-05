from typing import List

import requests
from bs4 import BeautifulSoup

from config.settings import URL_MAPPING
from product.models import UncommitedProduct

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \n"
    "Chrome/117.0.0.0 Safari/537.36"
}


def get_all_web_product() -> list[UncommitedProduct]:
    all_web_product: list[UncommitedProduct] = []
    # all_web_product.extend(parse_web_product_1(url=URL_MAPPING["wizkids"]))
    all_web_product.extend(parse_web_product_2(url=URL_MAPPING["dom_igor"]))

    return all_web_product


def create_soup(url) -> BeautifulSoup:
    sessinon = requests.Session()
    response = sessinon.get(url=url, headers=headers)
    html_content = response.text

    return BeautifulSoup(html_content, "html.parser")


def parse_web_product_1(url) -> List[UncommitedProduct]:
    soup = create_soup(url=url)

    result: list[UncommitedProduct] = []
    table = soup.find("table", class_="tablepress-id-108")
    if table is not None:
        tbody = table.find("tbody", class_="row-hover")
        if tbody is not None:
            results_table = tbody.find_all("tr")
        else:
            print("Table has not found")
    else:
        print("Table has not found")

    if results_table is not None:
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
                image = columns[3].img["src"]
            except Exception:
                image = None

            name = columns[2].get_text()

            if sku is not None:
                result.append(
                    UncommitedProduct(sku=sku, name=name, url_image=image, category_id=None)
                )
    else:
        print("Table has not found")
    
    return result


def parse_web_product_2(url) -> List[UncommitedProduct]:
    result: list[UncommitedProduct] = []

    all_products_link: list = []
    while url:
        soup = create_soup(url=url)
        products = soup.find_all("div", class_="product-anons")

        products_link: list = [
            product.find("a", class_="image")["href"] for product in products
        ]
        all_products_link.extend(products_link)

        pagination_container = soup.find("div", class_="links")
        next_page_link = pagination_container.find("a", string=">")

        if next_page_link:
            url = next_page_link["href"]
        else:
            break

    for product_link in all_products_link:
        soup = create_soup(url=product_link)

        product = soup.find("div", class_="product-right")
        name: str = (
            product.find("div", class_="product-title box-title")
            .find("h1")
            .text.strip()
        )
        articul_element = product.find("div", class_="minis_chars").find(
            "b", string="Артикул:"
        )
        sku: int = int(articul_element.find_next_sibling(string=True).strip())
        image = soup.find("div", class_="gallery-slider").find("img")["src"]

        result.append(
            UncommitedProduct(name=name, sku=sku, url_image=image, category_id=None)
        )

    return result
