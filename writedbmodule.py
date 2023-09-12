import csv
from data import UncommitedMiniatures
import requests


base_miniatures: list[UncommitedMiniatures] = []

# with open('list_new-TDSheet.csv', "r") as f:
#     lines = f.readlines()
#     for row in lines[1:]:
#         value = row.strip().split(',')
#         base_miniatures.append(UncommitedMiniatures(sku=int(value[0][3:]), name=value[1], image=None))
        
with open('list_new-TDSheet.csv', "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        row['sku'] = int(row['sku'][3:])
        row['image'] = None
        base_miniatures.append(UncommitedMiniatures(**row))
    
print(base_miniatures[0:2])        


class Image:
    def __init__(self, url):
        self.url = url

    def download_image(self):
        self.image_responce = requests.get(self.url)