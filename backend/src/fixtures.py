from injector import singleton, Injector

from apps.notifications.tasks import (
    INotificationAdapter,
    send_invite_to_client,
)
# noinspection PyProtectedMember
from project.containers import _init_container, _init_mediator


class DummyNotificationAdapter(INotificationAdapter):
    def send_invite_to_client(self, message: str) -> None:
        send_invite_to_client(message)


def init_dummy_container() -> Injector:
    container = _init_container()
    container.binder.bind(
        INotificationAdapter,
        to=DummyNotificationAdapter,
        scope=singleton,
    )
    _init_mediator(container)
    return container
