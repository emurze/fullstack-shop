import pytest
from injector import Injector

from apps.products.repositories import IProductRepository

# noinspection PyProtectedMember
from project.containers import _init_container
from seedwork.mediator import Mediator


@pytest.fixture(scope="function")
def container() -> Injector:
    return _init_container()


@pytest.fixture(scope="function")
def mediator(container: Injector) -> Mediator:
    return container.get(Mediator)


@pytest.fixture(scope="function")
def product_repo(container: Injector) -> IProductRepository:
    return container.get(IProductRepository)
