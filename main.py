from parser.services import get_all_web_product
from typing import Generator

from api.api_client import APIClient
from authentication import get_token
from config.settings import ADMIN_BASE_URL, ADMIN_PRODUCT_ADD, FILE_EXEL_NAME
from image_manager.models import Image
from image_manager.services import upload_image
from product.data_processor import DataProcessor
from product.models import Product, UncommitedProduct
from product.services import get_all_base_product

token, session = get_token()

all_web_product: list[UncommitedProduct] = get_all_web_product()
all_base_product: list[UncommitedProduct] = get_all_base_product(file=FILE_EXEL_NAME)

data_processor: DataProcessor = DataProcessor(
    web_list=all_web_product, base_list=all_base_product
)
matching_product: Generator[
    UncommitedProduct, None, None
] = data_processor.get_matching_products()
api_processor: APIClient = APIClient(
    base_url=ADMIN_BASE_URL, token=token, session=session
)


def main() -> None:
    for uncommited_product in matching_product:
        image: Image | None = upload_image(
            url_image=uncommited_product.url_image, token=token, session=session
        )
        data: Product = data_processor.create_product(
            web_product=uncommited_product, image=image
        )
        api_processor.send_post_request(endpoint=ADMIN_PRODUCT_ADD, data=data)


if __name__ == "__main__":
    main()
