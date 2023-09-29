import os

import requests
from image_manager.models import Image
from config.settings import (ADMIN_BASE_URL, ADMIN_FILE_UPLOAD, DIR_CATALOG,
                             DIR_FOTO, DIR_PROJECT)
import json

def upload_image(url_image, token, session) -> Image:
    try:
        web_image = requests.get(url=url_image)
        if web_image.status_code == 200:
            image_name = os.path.basename(url_image)
            print(f"✅⬇️ File successfully downloaded: {image_name}")
        else:
            print(f"❌ File download failed. HTTP status code: {web_image.status_code}")
    except Exception as e:
        print(f"❌ An error occurred while downloading a file {url_image}: {str(e)}")
        return

    params: dict = {"token": token, "directory": f"{DIR_FOTO}/{DIR_PROJECT}"}
    file: dict = {"file[]": (image_name, web_image.content, "image/png")}

    try:
        response = session.post(
            f"{ADMIN_BASE_URL}{ADMIN_FILE_UPLOAD}", params=params, files=file
        )
        response_content = json.loads(response.content)
        if response.status_code == 200:
            new_url_image: list = response_content["filepaths"]
            image: Image = Image(name={file['file[]'][0]}, url_image=new_url_image)
            print(Image)
            print(
                f"status code: {response.status_code}\n"
                f"✅⬆️ Image successfully uploaded: {file['file[]'][0]}"
            )
            return image

        else:
            print(f"❌ Image upload failed. HTTP status code: {response.status_code}")
    except Exception as e:
        print(
            f"❌ An error occurred while uploading an image to web site: {response.status_code} {str(e)}"
        )
