from staticfiles.field_text import FIELD
from dataclasses import dataclass

@dataclass
class FieldMiniature:
    DESCRIPTION: str = FIELD["DESCRIPTION"]
    DESCRIPTION_SHORT: str = FIELD["DESCRIPTION_SHORT"] 
    HTML_META_TITLE: str = FIELD["HTML_META_TITLE"]
    META_DESCRIPTION: str = FIELD["META_DESCRIPTION"]
    TAG_DESCRIPTION: str = FIELD["TAG_DESCRIPTION"]
