from dataclasses import dataclass

from staticfiles.field_text import FIELD

CATEGORY_MAPPING: dict = {
    "Main Category": 287,
    "Critical Role": 288,
    "D&D Nolzur's Marvelous Miniatures": 289,
    "Magic the Gathering": 290,
    "Pathfinder Deep Cuts": 291,
}


@dataclass
class FieldProduct:
    DESCRIPTION: str = FIELD["DESCRIPTION"]
    DESCRIPTION_SHORT: str = FIELD["DESCRIPTION_SHORT"]
    HTML_META_TITLE: str = FIELD["HTML_META_TITLE"]
    META_DESCRIPTION: str = FIELD["META_DESCRIPTION"]
    TAG_DESCRIPTION: str = FIELD["TAG_DESCRIPTION"]
