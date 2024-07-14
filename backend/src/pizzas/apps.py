from django.apps import AppConfig


class PizzasConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "pizzas"

    def ready(self) -> None:
        import pizzas.singals  # type: ignore
