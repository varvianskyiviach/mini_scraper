from datetime import date

from pydantic import BaseModel, Field


class UncommitedMiniatures(BaseModel):
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

class Miniatures(BaseModel):
    name: str = Field(serialization_alias="product_description[1][name]")
    name_alternative: str = Field(serialization_alias="upc")
    description: str = Field(serialization_alias="product_description[1][description]")
    description_short: str = Field(serialization_alias="product_description[1][meta_keyword]")
    html_meta_title: str = Field(serialization_alias="product_description[1][meta_title]")
    html_meta_h1: str = Field(serialization_alias="product_description[1][merta_h1]")
    meta_description: str = Field(serialization_alias="product_description[1][meta_description]")
    tag_description: str = Field(serialization_alias="product_description[1][tag]")
    
    model: int = Field(serialization_alias="model")
    sku: int = Field(serialization_alias="sku")
    stock_status_id: int = Field(serialization_alias="stock_status_id")
    date_available: date = Field(serialization_alias="date_available", default=date.today())
    sort_order: int = Field(serialization_alias="sort_order", default=10)
    status: int = Field(serialization_alias="status", default=1)
    
    manufacturer_id: int = Field(serialization_alias="manufacturer_id", default="")
    main_category_id: int = Field(serialization_alias="main_category_id", default="")
    product_category: int = Field(serialization_alias="product_category[]", default="")
    product_category: int = Field(serialization_alias="product_category[]", default="")
    product_store: int = Field(serialization_alias="product_store[]", default=1)
    image: str = Field(serialization_alias="image")

# mini = Miniatures(name="one")
# mini = mini.model_dump(by_alias=True)
# print(mini)