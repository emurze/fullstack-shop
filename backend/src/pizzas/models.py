from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models import Index


class Pizza(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image_url = models.ImageField(max_length=255)
    types = models.ManyToManyField("Type", related_name="pizzas")
    sizes = models.ManyToManyField("Size", related_name="pizzas")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(
        "Category",
        related_name="pizzas",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    rating = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[
            MaxValueValidator(10),
        ],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            Index(fields=["slug"]),
            Index(fields=["-created_at"]),
        ]
        verbose_name = "Pizza"
        verbose_name_plural = "Pizzas"

    def __str__(self) -> str:
        return self.title


class Type(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"

    def __str__(self) -> str:
        return self.title


class Size(models.Model):
    size = models.IntegerField(primary_key=True)

    class Meta:
        verbose_name = "Size"
        verbose_name_plural = "Sizes"

    def __str__(self) -> str:
        return str(self.size)


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.title
