from dataclasses import dataclass

from apps.products.repositories import IProductRepository
from seedwork.mediator import Mediator, command_handler


@dataclass(frozen=True)
class CreateProductCommand:
    title: str


@dataclass(frozen=True)
class ProductService:
    mediator: Mediator
    products: IProductRepository

    @command_handler
    def create_product(self, command: CreateProductCommand) -> None:
        print(f"{self.products=}")
