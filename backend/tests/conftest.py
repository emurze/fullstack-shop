import pytest

from config import AppConfig
from container import container

test_config = AppConfig(app_title="Test App")
container.config.override(test_config)


@pytest.fixture
def config() -> AppConfig:
    return test_config
