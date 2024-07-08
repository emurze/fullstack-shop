import pytest
from injector import Injector

# noinspection PyProtectedMember
from project.containers import _init_container
from seedwork.mediator import Mediator


@pytest.fixture(scope="function")
def container() -> Injector:
    return _init_container()


@pytest.fixture(scope="function")
def mediator(container: Injector) -> Mediator:
    return container.get(Mediator)
