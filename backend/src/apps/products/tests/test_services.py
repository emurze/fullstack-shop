import pytest
from faker import Faker

from apps.products.repositories import IProductRepository
from apps.products.services import (
    CreateProductCommand,
    DeleteProductCommand,
    UpdateProductCommand,
)
from seedwork.mediator import Mediator


@pytest.mark.integration
@pytest.mark.django_db(transaction=True)
class TestProductService:
    def setup_class(self) -> None:
        self.faker = Faker()

    def test_can_create(  # TODO: find solution to decompose arguments to self
        self,
        mediator: Mediator,
        product_repo: IProductRepository,
    ) -> None:
        title = self.faker.text(max_nb_chars=50)
        command = CreateProductCommand(title=title)

        product_id = mediator.handle(command)

        product = product_repo.get_by_id(product_id)
        assert product.id == product_id
        assert product.title == title

    def test_can_delete(
        self,
        mediator: Mediator,
        product_repo: IProductRepository,
    ) -> None:
        title = self.faker.text(max_nb_chars=50)
        command = CreateProductCommand(title=title)
        product_id = mediator.handle(command)

        command = DeleteProductCommand(id=product_id)
        mediator.handle(command)

        assert product_repo.count() == 0

    def test_can_delete_nothing_quietly(
        self,
        mediator: Mediator,
        product_repo: IProductRepository,
    ) -> None:
        ido = self.faker.random_int()
        command = DeleteProductCommand(id=ido)
        mediator.handle(command)

    def test_can_update_product(
        self,
        mediator: Mediator,
        product_repo: IProductRepository,
    ) -> None:
        title = self.faker.text(max_nb_chars=50)
        command = CreateProductCommand(title=title)
        product_id = mediator.handle(command)

        new_title = self.faker.text(max_nb_chars=50)
        command = UpdateProductCommand(id=product_id, title=new_title)
        mediator.handle(command)

        product = product_repo.get_by_id(product_id)
        assert product.title == new_title
