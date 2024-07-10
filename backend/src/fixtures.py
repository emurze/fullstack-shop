from injector import singleton, Injector

from apps.notifications.tasks import (
    INotificationAdapter,
    DummyNotificationAdapter,
)
# noinspection PyProtectedMember
from project.containers import _init_container, _init_mediator


def init_dummy_container() -> Injector:
    container = _init_container()
    container.binder.bind(
        INotificationAdapter,
        to=DummyNotificationAdapter,
        scope=singleton,
    )
    _init_mediator(container)
    return container
