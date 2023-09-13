import csv
from typing import List

from config.settings import STATIC_ROOT
from miniatures.models import UncommitedMiniatures


def get_base_miniatures() -> List[UncommitedMiniatures]:
    base_miniatures: list[UncommitedMiniatures] = []

    # with open('list_new-TDSheet.csv', "r") as f:
    #     lines = f.readlines()
    #     for row in lines[1:]:
    #         value = row.strip().split(',')
    #         base_miniatures.append(UncommitedMiniatures(sku=int(value[0][3:]), name=value[1], image=None))

    with open(f'{STATIC_ROOT}/list_new-TDSheet.csv', "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            row['sku'] = int(row['sku'][3:])
            row['image'] = None
            base_miniatures.append(UncommitedMiniatures(**row))

    return base_miniatures
