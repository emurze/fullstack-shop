from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

from pizzas.models import Pizza


@receiver(post_save, sender=Pizza)
def set_slug(sender: type[Pizza], instance: Pizza, **_) -> None:
    if instance.slug == "":
        instance.slug = slugify(f"{instance.title}-{instance.id}")
