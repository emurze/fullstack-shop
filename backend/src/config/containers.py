from collections.abc import Callable
from functools import lru_cache
from typing import Any

from injector import Module, Injector, provider, singleton, Binder, inject

from base.uows import DjangoUnitOfWork, IUnitOfWork


def singleton_provider(fn: Callable) -> Callable:
    return singleton(provider(fn))


def inject_service(binder: Binder, service_class: Any):
    try:
        inject(service_class)
    except AttributeError:
        service = service_class()
        binder.bind(service_class, service)


class MainModule(Module):
    def configure(self, binder: Binder) -> None:
        pass

    @singleton_provider
    def provider_uow(self) -> IUnitOfWork:
        return DjangoUnitOfWork()


def _init_container() -> Injector:
    return Injector(MainModule())


@lru_cache(1)
def get_container() -> Injector:
    return _init_container()
