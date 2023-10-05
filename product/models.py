from datetime import date

from pydantic import BaseModel, Field

from product.constants import CATEGORY_MAPPING, FieldProduct


class UncommitedProduct(BaseModel):
    sku: int
    name: str
    url_image: str | None
    category_id: list[int | None]

    def __str__(self) -> str:
        return "\n".join(
            (
                f"name: {self.name},",
                "=================",
                f"sku: {self.sku},",
                f"url_image: {self.url_image},",
                f"category_id: {self.category_id}",
            )
        )


class Product(BaseModel):
    name: str = Field(serialization_alias="product_description[1][name]")
    name_alternative: str = Field(serialization_alias="upc")
    description: str = Field(
        serialization_alias="product_description[1][description]",
        default=FieldProduct.DESCRIPTION,
    )
    description_short: str = Field(
        serialization_alias="product_description[1][meta_keyword]",
        default=FieldProduct.DESCRIPTION_SHORT,
    )
    html_meta_title: str = Field(
        serialization_alias="product_description[1][meta_title]",
        default=FieldProduct.HTML_META_TITLE,
    )
    html_meta_h1: str = Field(serialization_alias="product_description[1][meta_h1]")
    meta_description: str = Field(
        serialization_alias="product_description[1][meta_description]",
        default=FieldProduct.META_DESCRIPTION,
    )
    tag_description: str = Field(
        serialization_alias="product_description[1][tag]",
        default=FieldProduct.TAG_DESCRIPTION,
    )

    model: str = Field(serialization_alias="model")
    sku: str = Field(serialization_alias="sku")
    novelty: int = Field(serialization_alias="novelty", default=1)
    minimum: int = Field(serialization_alias="minimum", default=1)
    subtract: int = Field(serialization_alias="subtract", default=1)
    shipping: int = Field(serialization_alias="shipping", default=1)
    stock_status_id: int = Field(serialization_alias="stock_status_id", default=5)
    date_available: date = Field(
        serialization_alias="date_available", default=date.today()
    )
    sort_order: int = Field(serialization_alias="sort_order", default=10)
    status: int = Field(serialization_alias="status", default=1)

    manufacturer_id: int = Field(serialization_alias="manufacturer_id", default=88)
    main_category_id: int = Field(
        serialization_alias="main_category_id",
        default=CATEGORY_MAPPING.get("Main Category", 287),
    )
    product_category: list[int] = Field(
        serialization_alias="product_category[]",
        default=[CATEGORY_MAPPING.get("Main Category")],
    )
    product_store: int = Field(serialization_alias="product_store[]", default=0)
    url_image: list[str] = Field(serialization_alias="image")
