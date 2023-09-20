import requests


class APIClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token
        
    def send_post_request(self, params, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, params=params, data=data)
        return response.text
