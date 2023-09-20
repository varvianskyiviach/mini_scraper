from parser.services import get_all_web_miniatures

from image_manager.services import upload_image
from miniatures.models import UncommitedMiniatures
from miniatures.services import get_all_base_miniatures
from miniatures.models import Miniatures
from typing import Generator

class DataProcessor:
    def __init__(self, web_list: list, base_list: list):
        self.web_list = web_list
        self.base_list = base_list
        

    def get_miniatures_from_lists(self) -> Generator[UncommitedMiniatures, None, None]:
        count = 0
        for base_mini in self.base_list:
            if count > 10:
                break
            for web_mini in self.web_list:
                if base_mini.sku == web_mini.sku:
                    yield web_mini
                    count += 1
                    break


    def create_miniature(self, payload) -> Miniatures:
        return Miniatures(**payload)
    















