from parser.services import get_all_web_miniatures

from api.api_client import APIClient
from miniatures.data_processor import DataProcessor
from miniatures.models import UncommitedMiniatures
from miniatures.services import get_all_base_miniatures
from authentication import get_token
from image_manager.services import upload_image
from config.settings import FILE_EXEL_NAME

token, session = get_token()

all_web_miniatures: list[UncommitedMiniatures] = get_all_web_miniatures()
all_base_miniatures: list[UncommitedMiniatures] = get_all_base_miniatures(file=FILE_EXEL_NAME)

data_processor: DataProcessor = DataProcessor(web_list=all_web_miniatures, base_list=all_base_miniatures)
miniatures_uncommited_list = data_processor.get_miniatures_from_lists()

for miniatures in miniatures_uncommited_list:
    upload_image(url_image=miniatures.image, token=token, session=session)

