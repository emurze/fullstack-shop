import abc

from celery import shared_task
from django.core.mail import send_mail


class INotificationAdapter(abc.ABC):
    @abc.abstractmethod
    def send_invite_to_client(self, message: str) -> None: ...


class NotificationAdapter(INotificationAdapter):
    def send_invite_to_client(self, message: str) -> None:
        send_invite_to_client.delay(message)


@shared_task
def send_invite_to_client(message: str) -> None:
    send_mail(
        "Subject here",
        f"{message}",
        "from@example.com",
        ["to@example.com"],
        fail_silently=False,
    )
