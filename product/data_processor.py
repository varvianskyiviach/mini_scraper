from typing import Generator

from product.models import Product, UncommitedProduct
from image_manager.models import Image


class DataProcessor:
    def __init__(self, web_list: list, base_list: list):
        self.web_list = web_list
        self.base_list = base_list

    def get_matching_products(self) -> Generator[UncommitedProduct, None, None]:
        # count = 0
        for base_product in self.base_list:
            # if base_product.sku == 90344:
                # if count >= 1:
                #     break
            for web_product in self.web_list:
                if base_product.sku == web_product.sku:
                    base_product.url_image = web_product.url_image
                    print(base_product)
                    yield base_product
                    # count += 1
                    break

    def create_product(self, web_product: UncommitedProduct, image: Image) -> Product:
        payload: dict = {
            "name": web_product.name,
            "name_alternative": web_product.name,
            "html_meta_h1": web_product.name,
            "model": str(web_product.sku),
            "sku": str(web_product.sku),
            "product_category": web_product.category_id,
            "url_image": image.url_image if image is not None else []
        }
        try:
            product: Product = Product(**payload)
            print(f"✅ Product successfully created: {product.name}")
            return product
        except Exception as e:
            print(f" ❌ Could not create a product: {payload['name']}")
            print(f"❗️{str(e)}")
