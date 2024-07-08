from dataclasses import dataclass

from apps.products.models import Product
from apps.products.repositories import IProductRepository
from seedwork.mediator import Mediator


@dataclass(frozen=True)
class CreateProductCommand:
    title: str


@dataclass(frozen=True)
class DeleteProductCommand:
    id: int


@dataclass(frozen=True)
class UpdateProductCommand:
    id: int
    title: str


@dataclass(frozen=True)
class ProductService:
    mediator: Mediator
    products: IProductRepository

    def create_product(self, command: CreateProductCommand) -> int:
        product = Product(title=command.title)
        self.products.add(product)
        return product.id

    def delete_product(self, command: DeleteProductCommand) -> None:
        self.products.delete_by_id(command.id)

    def update_product(self, command: UpdateProductCommand) -> None:
        product = self.products.get_by_id(command.id, for_update=True)
        product.update(title=command.title)
