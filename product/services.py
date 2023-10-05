import csv
import re
from typing import List

from config.settings import STATIC_ROOT
from product.constants import CATEGORY_MAPPING
from product.models import UncommitedProduct


def get_category_name(text: str) -> str | None:
    match = re.search(r" - (.*?) - ", text)
    if match:
        category_name = match.group(1).strip()
        try:
            match = re.search(r"^(.*?) Unpainted Miniatures", category_name)
            if match:
                category_name = match.group(1)
            else:
                match = re.search(r"^(.*?) Wave", category_name)
                if match:
                    category_name = match.group(1)
        except AttributeError:
            raise AttributeError

        return category_name
    return None


def get_all_base_product(file) -> List[UncommitedProduct]:
    all_base_product: list[UncommitedProduct] = []

    # with open('list_new-TDSheet.csv', "r") as f:
    #     lines = f.readlines()
    #     for row in lines[1:]:
    #         value = row.strip().split(',')
    #         base_product.append(UncommitedProduct(sku=int(value[0][3:]), name=value[1], image=None))

    with open(f"{STATIC_ROOT}/{file}", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            name: str = row["name"]
            category_name: str | None = get_category_name(text=name)

            row["sku"] = int(row["sku"][3:])
            row["url_image"] = None
            row["category_id"] = [
                CATEGORY_MAPPING.get("Main Category"),
                CATEGORY_MAPPING.get(category_name),
            ]

            all_base_product.append(UncommitedProduct(**row))

    return all_base_product
