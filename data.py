from pydantic import BaseModel

class Miniatures(BaseModel):
    article: int
    name: str
    image: str | None

