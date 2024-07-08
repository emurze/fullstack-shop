from autoslug import AutoSlugField
from django.db import models
from django.db.models import Manager

from seedwork.models import AggregateRoot


class Product(AggregateRoot):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(
        unique=True, db_index=True, populate_from="title"
    )  # TODO: Remove lib set trigger
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Manager()

    class Meta:
        ordering = ["-created_at"]

    def update(self, title: str) -> None:
        self.title = title

    def __str__(self) -> str:
        return self.title
