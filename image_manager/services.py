import json
import os

import requests

from config.settings import (ADMIN_BASE_URL, ADMIN_FILE_UPLOAD, DIR_FOTO,
                             DIR_PROJECT)
from image_manager.models import Image
from requests import Session

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \n"
    "Chrome/117.0.0.0 Safari/537.36"
}


def upload_image(url_image: str | None, token: str, session: Session) -> Image | None:
    if url_image is not None:
        try:
            web_image = requests.get(url=url_image, headers=headers)
            if web_image.status_code == 200:
                image_name = os.path.basename(url_image)
                print(f"✅⬇️ File successfully downloaded: {image_name}")
            else:
                print(f"❌ File download failed. HTTP status code: {web_image.status_code}")
                return None
        except Exception as e:
            print(f"❌ An error occurred while downloading a file {url_image}: {str(e)}")
            return None
    else:
        return None
    
    params: dict = {"token": token, "directory": f"{DIR_FOTO}/{DIR_PROJECT}"}
    file: dict = {"file[]": (image_name, web_image.content, "image/jpeg")}

    try:
        response = session.post(
            f"{ADMIN_BASE_URL}{ADMIN_FILE_UPLOAD}", params=params, files=file
        )
        response_content = json.loads(response.content)
        if response.status_code == 200:
            new_url_image: list = response_content["filepaths"]
            image: Image = Image(name=str({file["file[]"][0]}), url_image=new_url_image)
            print(Image)
            print(
                f"status code: {response.status_code}\n"
                f"✅⬆️ Image successfully uploaded: {file['file[]'][0]}"
            )
            return image

        else:
            print(f"❌ Image upload failed. HTTP status code: {response.status_code}")
            return None
    except Exception as e:
        print(
            f"❌ An error occurred while uploading an image to web site: {response.status_code} {str(e)}"
        )
        return None