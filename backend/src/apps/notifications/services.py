from dataclasses import dataclass

from apps.notifications.tasks import INotificationAdapter


@dataclass(frozen=True)
class SendInviteCommand:
    message: str


@dataclass(frozen=True)
class NotificationService:
    notification_adapter: INotificationAdapter

    def send_invite_to_client(self, command: SendInviteCommand) -> None:
        self.notification_adapter.send_invite_to_client(command.message)
