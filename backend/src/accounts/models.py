from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class Account(AbstractUser):
    description = models.TextField(
        null=True,
        verbose_name="Description",
        max_length=120,
    )
    photo = models.ImageField(
        upload_to="accounts/%Y/%m/%d/",
        blank=True,
        null=True,
        verbose_name="Avatar",
    )
    birthday = models.DateField(null=True, blank=True)

    objects = UserManager()

    def __str__(self) -> str:
        return self.username
