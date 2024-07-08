from functools import lru_cache

from project.containers import get_container
from seedwork.mediator import Mediator


@lru_cache(1)
def get_mediator() -> Mediator:
    container = get_container()
    return container.get(Mediator)
