import os

import requests

from ftp_server.services import FTPManager


class ImageManager:

    def __init__(self, ftp_manager: FTPManager = None) -> None:

        # if not isinstance(ftp_manager, FTPManager):
        #     raise ValueError("ftp_manager must be an instance of FTPManager")
        self.ftp_manager = ftp_manager

    def download_image(self, source_url, local_path) -> None:

        try:
            responce = requests.get(source_url)
            if responce.status_code == 200:
                with open(local_path, 'wb') as file:
                    file.write(responce.content)
                print(f"Image successfully downloaded: {local_path}")

            else:
                print(
                    f"Image download failed. HTTP status code: {responce.status_code}")
        except Exception as e:
            print(
                f"An error occurred while downloading an image {source_url}: {str(e)}")

    def upload_image(self, local_path, remote_path) -> None:

        try:
            with open(local_path, "rb") as file:
                self.ftp_manager.storbinary(f'STOR {remote_path}', file)
            print(f"Image successfully uploaded to FTP server: {remote_path}")
        except Exception as e:
            print(
                f"An error occurred while uploading an image to FTP server {remote_path}: {str(e)}")

    def remove_image(self, local_path) -> None:

        try:
            os.remove(local_path)
            print(f"Image {local_path} has been successfully removed")
        except OSError as e:
            print(
                f"An error occurred while removing image {local_path}: {str(e)}")
