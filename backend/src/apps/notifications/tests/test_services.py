import pytest
from django.core import mail
from faker import Faker

from apps.notifications.services import SendInviteCommand
from seedwork.mediator import Mediator


@pytest.mark.integration
@pytest.mark.django_db(transaction=True)
class TestNotificationsService:
    def setup_class(self) -> None:
        self.faker = Faker()

    def test_can_send_invite(self, mediator: Mediator, container) -> None:
        message = self.faker.text(max_nb_chars=50)
        command = SendInviteCommand(message=message)
        mediator.handle(command)

        assert len(mail.outbox) == 1
        assert mail.outbox[0].subject == "Subject here"
