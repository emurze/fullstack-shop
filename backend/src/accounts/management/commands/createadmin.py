import logging

from django.conf import settings
from django.core.management import BaseCommand

from accounts.models import Account

lg = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "This command creates superuser"

    def handle(self, *_, **__) -> None:
        if not Account.objects.exists():
            account = Account.objects.create_superuser(
                username=settings.ADMIN_NAME,
                email=settings.ADMIN_EMAIL,
                password=settings.ADMIN_PASSWORD,
            )
            lg.debug(f"Admin {account.username} was created.")
