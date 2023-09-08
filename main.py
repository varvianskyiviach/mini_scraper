import requests
from bs4 import BeautifulSoup
from data import Miniatures

url = "https://wizkids.com/wp-json/wp/v2/pages/6899"

responce = requests.get(url).json()

html_content = responce["content"]["rendered"]

soup = BeautifulSoup(html_content, "html.parser")
table = soup.find("table", class_="tablepress-id-108")

rows_table = table.find("tbody", class_="row-hover").find_all("tr")

miniatures: list[Miniatures] = []

for row in rows_table:
    columns = row.find_all("td")
    
    try:
        article = int(columns[0].get_text())
    except:
        try:
            article = int(columns[1].get_text())
        except:
            article = None
    
    try:
        image = columns[3].img['src']
    except:
        image = None
    
    name = columns[2].get_text()
       
    if article is not None:

        miniatures.append(Miniatures(article=article, name=name, image=image))

print(len(miniatures))
# for mini in miniatures:
    # print(len)
    # print(f"article - {mini.article}, name - {mini.name}, image - {mini.image}")
