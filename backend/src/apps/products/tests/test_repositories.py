import pytest
from faker import Faker

from apps.products.models import Product
from apps.products.repositories import IProductRepository, ProductRepository


@pytest.mark.integration
@pytest.mark.django_db(transaction=True, reset_sequences=True)
class TestProductRepository:
    def setup_class(self) -> None:
        self.faker: Faker = Faker()
        self.products: IProductRepository = ProductRepository()

    def test_can_add(self) -> None:
        title = self.faker.text(max_nb_chars=50)
        product = Product(title=title)
        product_id = self.products.add(product)
        assert self.products.get_by_id(product_id)

    def test_can_get_by_id(self) -> None:
        title = self.faker.text(max_nb_chars=50)
        product = Product(title=title)
        product_id = self.products.add(product)

        product = self.products.get_by_id(product_id)
        assert product.title == title

    def test_get_by_id_not_found(self) -> None:
        product_id = self.faker.random_int()
        product = self.products.get_by_id(product_id)
        assert product is None

    def test_can_count(self) -> None:
        title = self.faker.text(max_nb_chars=50)
        self.products.add(Product(title=title))
        self.products.add(Product(title=title))

        products_quantity = self.products.count()
        assert products_quantity == 2

    def test_can_delete_by_id(self) -> None:
        title = self.faker.text(max_nb_chars=50)
        product = Product(title=title)
        self.products.add(product)

        self.products.delete_by_id(product.id)
        assert self.products.get_by_id(product.id) is None
