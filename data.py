from pydantic import BaseModel

class UncommitedMiniatures(BaseModel):
    sku: int
    name: str
    image: str | None

