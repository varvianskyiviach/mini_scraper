from pydantic import BaseModel


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
