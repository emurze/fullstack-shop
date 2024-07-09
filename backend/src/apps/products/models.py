from django.db import models
from django.db.models import Manager, Index
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

from seedwork.models import AggregateRoot


class Product(AggregateRoot):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Manager()

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            Index(fields=["slug"]),
            Index(fields=["-created_at"]),
        ]

    def update(self, title: str) -> None:
        self.title = title

    def __str__(self) -> str:
        return self.title


@receiver(post_save, sender=Product)
def set_slug(sender: type[Product], instance: Product, **_) -> None:
    if instance.slug == "":
        instance.slug = slugify(f"{instance.title}-{instance.id}")
