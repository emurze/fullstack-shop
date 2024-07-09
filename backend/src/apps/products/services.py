from dataclasses import dataclass

from apps.notifications.services import SendInviteCommand
from apps.products.models import Product
from apps.products.repositories import IProductRepository
from seedwork.mediator import command_handler, BasicMediator


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
    mediator: BasicMediator
    products: IProductRepository

    @command_handler
    def create_product(self, command: CreateProductCommand) -> int:
        product = Product(title=command.title)
        self.products.add(product)

        command = SendInviteCommand(
            message=f"Author of product <{command.title}> is invited"
        )
        self.mediator.handle(command)

        return product.id

    @command_handler
    def delete_product(self, command: DeleteProductCommand) -> None:
        self.products.delete_by_id(command.id)

    @command_handler
    def update_product(self, command: UpdateProductCommand) -> None:
        product = self.products.get_by_id(command.id, for_update=True)
        product.update(title=command.title)
