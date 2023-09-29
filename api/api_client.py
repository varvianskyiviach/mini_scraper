from requests import Session

from product.models import Product


class APIClient:
    def __init__(self, base_url: str, token: str, session: Session):
        self.base_url = base_url
        self.token = token
        self.session = session

    def send_post_request(self, endpoint: str, data: Product):
        form_data: dict = data.model_dump(by_alias=True)
        url_create_object = f"{self.base_url}{endpoint}"
        params = {
            "token": self.token,
        }
        try:
            response = self.session.post(url_create_object, params=params, data=form_data)
            if response.status_code == 200:
                print(
                    f"✅ Object successfully created: {form_data['product_description[1][name]']} \n"
                    f"{url_create_object}"
                )
            else:
                print(
                    f"❌ Error occurred during object creation: {response.status_code} \n"
                )
        except Exception as e:
            print(
                f"❌ Could not create an object: {form_data['product_description[1][name]']} \n"
            )
            print(f"❗️{str(e)}")
