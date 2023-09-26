import os

import requests

from config.settings import (ADMIN_BASE_URL, ADMIN_FILE_UPLOAD, DIR_CATALOG,
                             DIR_FOTO, DIR_PROJECT)


def upload_image(url_image, token, session):
    try:
        image = requests.get(url=url_image)
        if image.status_code == 200:
            image_name = os.path.basename(url_image)
            print(f"✔️⬇️ File successfully downloaded: {image_name}")
        else:
            print(f"❌ File download failed. HTTP status code: {image.status_code}")
    except Exception as e:
        print(f"❌ An error occurred while downloading a file {url_image}: {str(e)}")

    params: dict = {"token": token, "directory": f"{DIR_FOTO}/{DIR_PROJECT}"}
    file: dict = {"file[]": (image_name, image.content, "image/png")}

    try:
        response = session.post(
            f"{ADMIN_BASE_URL}{ADMIN_FILE_UPLOAD}", params=params, files=file
        )
        if response.status_code == 200:
            print(
                f"status code: {response.status_code}\n"
                f"✅⬆️ Image successfully uploaded: {file['file[]'][0]}"
            )

            return f"{DIR_CATALOG}/{params['directory']}/{file['file[]'][0]}"

        else:
            print(f"❌ Image upload failed. HTTP status code: {response.status_code}")
    except Exception as e:
        print(
            f"❌ An error occurred while uploading an image to web site: {response.status_code} {str(e)}"
        )
