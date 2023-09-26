from typing import Generator

from miniatures.models import Miniature, UncommitedMiniature


class DataProcessor:
    def __init__(self, web_list: list, base_list: list):
        self.web_list = web_list
        self.base_list = base_list

    def get_matching_miniatures(self) -> Generator[UncommitedMiniature, None, None]:
        count = 0
        for base_mini in self.base_list:
            if count >= 1:
                break
            for web_mini in self.web_list:
                if base_mini.sku == web_mini.sku:
                    yield web_mini
                    count += 1
                    break

    def create_miniature(
        self, web_miniature: UncommitedMiniature, new_url: str
    ) -> Miniature:
        payload: dict = {
            "name": web_miniature.name,
            "name_alternative": web_miniature.name,
            "html_meta_h1": web_miniature.name,
            "model": str(web_miniature.sku),
            "sku": str(web_miniature.sku),
            "image": new_url,
        }
        try:
            miniature = Miniature(**payload)
            print(f"✅ Miniature successfully created: {miniature.name}")
            return miniature
        except Exception as e:
            print(f" ❌ Could not create a Miniature: {payload['name']}")
            print(f"❗️{str(e)}")
