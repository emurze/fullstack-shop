from collections.abc import Callable
from functools import lru_cache

from injector import Module, Injector, provider, singleton, Binder

from apps.products.repositories import ProductRepository, IProductRepository
from apps.products.services import ProductService
from seedwork.mediator import Mediator
from seedwork.uows import DjangoUnitOfWork, IUnitOfWork


def singleton_provider(fn: Callable) -> Callable:
    return singleton(provider(fn))


class MainModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(IProductRepository, to=ProductRepository, scope=singleton)

    @singleton_provider
    def provider_uow(self, product_repo: IProductRepository) -> IUnitOfWork:
        return DjangoUnitOfWork(product_repo)

    @singleton_provider
    def provide_mediator(
        self,
        uow: IUnitOfWork,
        container: Injector,
    ) -> Mediator:
        return Mediator(uow=uow, container=container)


def init_mediator(container: Injector) -> Mediator:
    mediator = container.get(Mediator)
    mediator.register_service_commands(ProductService)
    return mediator


@lru_cache(1)
def get_container() -> Injector:
    return _init_container()


def _init_container() -> Injector:
    container = Injector(MainModule())
    init_mediator(container)
    return container
