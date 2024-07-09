import django_filters

from apps.products.models import Product


class ProductFilter(django_filters.FilterSet):
    created_at = django_filters.DateFilter(
        field_name="created_at",
        lookup_expr="date",
    )
    updated_at = django_filters.DateFilter(
        field_name="updated_at",
        lookup_expr="date",
    )

    class Meta:
        model = Product
        fields = (
            "title",
            "created_at",
            "updated_at",
        )


# class CategoryFilter(django_filters.FilterSet):
#     title = django_filters.DateFilter(field_name="title")
#
#     class Meta:
#         model = Category
#         fields = ("title",)
