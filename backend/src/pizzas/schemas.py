from pydantic import BaseModel, ConfigDict


class PizzaSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    imageUrl: str
    title: str
    types: list[int]
    sizes: list[int]
    price: int
    category: int
    rating: int
