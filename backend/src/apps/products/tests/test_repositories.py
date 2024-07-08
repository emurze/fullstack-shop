import pytest
from django.utils.text import slugify
from faker import Faker

from apps.products.models import Product
from apps.products.repositories import IProductRepository, ProductRepository


@pytest.mark.django_db
@pytest.mark.integration
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
        assert product.slug == slugify(title)

    def test_get_by_id_not_found(self) -> None:
        product_id = self.faker.random_int()

        product = self.products.get_by_id(product_id)

        assert product is None

    def test_can_count(self) -> None:
        title = self.faker.text(max_nb_chars=50)
        self.products.add(Product(title=title))
        self.products.add(Product(title=f"{title}_unique"))

        products_quantity = self.products.count()

        assert products_quantity == 2

    def test_can_delete_by_id(self) -> None:
        title = self.faker.text(max_nb_chars=50)
        product = Product(title=title)
        self.products.add(product)

        self.products.delete_by_id(product.id)

        assert self.products.get_by_id(product.id) is None
