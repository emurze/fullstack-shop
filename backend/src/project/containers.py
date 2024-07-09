from collections.abc import Callable
from functools import lru_cache

from injector import Module, Injector, provider, singleton, Binder

from apps.notifications.services import NotificationService
from apps.notifications.tasks import INotificationAdapter, NotificationAdapter
from apps.products.repositories import ProductRepository, IProductRepository
from apps.products.services import ProductService
from seedwork.mediator import Mediator, BasicMediator
from seedwork.uows import DjangoUnitOfWork, IUnitOfWork


def singleton_provider(fn: Callable) -> Callable:
    return singleton(provider(fn))


class MainModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(IProductRepository, to=ProductRepository, scope=singleton)
        binder.bind(
            INotificationAdapter,
            to=NotificationAdapter,
            scope=singleton,
        )

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

    @singleton_provider
    def provider_basic_mediator(
        self,
        mediator: Mediator,
        container: Injector,
    ) -> BasicMediator:
        return BasicMediator(container, mediator.command_map)


def _init_mediator(container: Injector) -> Mediator:
    mediator = container.get(Mediator)
    mediator.register_service_commands(ProductService)
    mediator.register_service_commands(NotificationService)
    return mediator


def _init_container() -> Injector:
    return Injector(MainModule())


@lru_cache(1)
def get_container() -> Injector:
    container = _init_container()
    _init_mediator(container)
    return container
