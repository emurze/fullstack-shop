import pytest
from injector import Injector

from fixtures import init_dummy_container


@pytest.fixture(scope="function")
def container() -> Injector:
    return init_dummy_container()
