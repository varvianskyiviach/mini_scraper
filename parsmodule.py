import requests
from bs4 import BeautifulSoup
from data import UncommitedMiniatures
from typing import List

url = "https://wizkids.com/wp-json/wp/v2/pages/6899"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
}
session = requests.Session()
responce = session.get(url, headers=headers).json()


def parse_mode(responce) -> List[UncommitedMiniatures]:

    html_content = responce["content"]["rendered"]

    soup = BeautifulSoup(html_content, "html.parser")
    table = soup.find("table", class_="tablepress-id-108")
    results_table = table.find("tbody", class_="row-hover").find_all("tr")

    all_web_miniatures: list[UncommitedMiniatures] = []

    for row in results_table:
        columns = row.find_all("td")
        try:
            sku = int(columns[0].get_text())
        except:
            try:
                sku = int(columns[1].get_text())
            except:
                sku = None
        try:
            image = columns[3].img['src']
        except:
            image = None

        name = columns[2].get_text()

        if sku is not None:
            all_web_miniatures.append(UncommitedMiniatures(
                sku=sku, name=name, image=image))

    return all_web_miniatures


import csv
from data import UncommitedMiniatures

base_miniatures: list[UncommitedMiniatures] = []
        
with open('list_new-TDSheet.csv', "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        row['sku'] = int(row['sku'][3:])
        row['image'] = None
        base_miniatures.append(UncommitedMiniatures(**row))
    
print(base_miniatures[0:2])  