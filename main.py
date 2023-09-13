from parser.parser import parse_mode

from config.settings import (FTP_HOST, FTP_PASSWORD, FTP_USERNAME,
                             STATIC_ROOT_IMAGES)
from ftp_server.services import FTPManager
from image_manager.repository import ImageManager
from miniatures.models import UncommitedMiniatures
from miniatures.services import get_base_miniatures


def main_script():

    all_web_miniatures: list[UncommitedMiniatures] = parse_mode()
    base_miniatures: list[UncommitedMiniatures] = get_base_miniatures()

    count = 0
    for base_mini in base_miniatures:
        if count > 10:
            break
        for index, web_mini in enumerate(all_web_miniatures):
            if base_mini.sku == web_mini.sku:
                image_filename = f"{web_mini.sku}_image_{index}.png"
                with FTPManager(FTP_HOST, FTP_USERNAME, FTP_PASSWORD) as ftp_server:
                    image_manager = ImageManager(ftp_manager=ftp_server)
                    image_manager.download_image(web_mini.image, STATIC_ROOT_IMAGES / image_filename)
            count += 1
            break
