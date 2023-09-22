from datetime import date

from pydantic import BaseModel, Field
from miniatures.constants import FieldMiniature

class UncommitedMiniature(BaseModel):
    sku: int
    name: str
    image: str | None

    def __repr__(self) -> str:
        return "\n".join(
            (
                f"sku: {self.sku}",
                f"name: {self.name}",
            )
        )

class Miniature(BaseModel):
    name: str = Field(serialization_alias="product_description[1][name]")
    name_alternative: str = Field(serialization_alias="upc")
    description: str = Field(serialization_alias="product_description[1][description]", default=FieldMiniature.DESCRIPTION)
    description_short: str = Field(serialization_alias="product_description[1][meta_keyword]", default=FieldMiniature.DESCRIPTION_SHORT)
    html_meta_title: str = Field(serialization_alias="product_description[1][meta_title]", default=FieldMiniature.HTML_META_TITLE)
    html_meta_h1: str = Field(serialization_alias="product_description[1][meta_h1]")
    meta_description: str = Field(serialization_alias="product_description[1][meta_description]", default=FieldMiniature.META_DESCRIPTION)
    tag_description: str = Field(serialization_alias="product_description[1][tag]", default=FieldMiniature.TAG_DESCRIPTION)
    
    model: str = Field(serialization_alias="model")
    sku: str = Field(serialization_alias="sku")
    novelty: int = Field(serialization_alias="novelty", default=1)
    minimum: int = Field(serialization_alias="minimum", default=1)
    subtract: int = Field(serialization_alias="subtract", default=1)
    shipping: int = Field(serialization_alias="shipping", default=1)
    stock_status_id: int = Field(serialization_alias="stock_status_id", default=5)
    date_available: date = Field(serialization_alias="date_available", default=date.today())
    sort_order: int = Field(serialization_alias="sort_order", default=10)
    status: int = Field(serialization_alias="status", default=1)
    
    manufacturer_id: int = Field(serialization_alias="manufacturer_id", default=88)
    main_category_id: int = Field(serialization_alias="main_category_id", default=270)
    product_category: int = Field(serialization_alias="product_category[]", default=270)
    product_category: int = Field(serialization_alias="product_category[]", default=271)
    product_store: int = Field(serialization_alias="product_store[]", default=1)
    image: str = Field(serialization_alias="image")
