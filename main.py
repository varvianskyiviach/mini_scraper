from parser.services import get_all_web_miniatures

from api.api_client import APIClient
from authentication import get_token
from config.settings import FILE_EXEL_NAME, ADMIN_BASE_URL, ADMIN_PRODUCT_ADD
from image_manager.services import upload_image
from miniatures.data_processor import DataProcessor
from miniatures.models import UncommitedMiniature, Miniature
from miniatures.services import get_all_base_miniatures
from typing import Generator

token, session = get_token()

all_web_miniatures: list[UncommitedMiniature] = get_all_web_miniatures()
all_base_miniatures: list[UncommitedMiniature] = get_all_base_miniatures(file=FILE_EXEL_NAME)

data_processor: DataProcessor = DataProcessor(web_list=all_web_miniatures, base_list=all_base_miniatures)
matching_miniatures: Generator[UncommitedMiniature, None, None] = data_processor.get_matching_miniatures()
api_processor: APIClient = APIClient(base_url=ADMIN_BASE_URL, token=token, session=session)

def main():
    for miniature in matching_miniatures:
        new_url_image_on_web: str = upload_image(url_image=miniature.image, token=token, session=session)
        
        data: Miniature = data_processor.create_miniature(miniature, new_url_image_on_web)
        data = data.model_dump(by_alias=True)
        print(data)
        api_processor.send_post_request(endpoint=ADMIN_PRODUCT_ADD, data=data)

if __name__ == "__main__":
    main()
