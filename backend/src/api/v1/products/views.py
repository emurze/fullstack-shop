from rest_framework.viewsets import ModelViewSet

from api.dependencies import get_mediator
from api.v1.products.filters import ProductFilter
from api.v1.products.serializers import ProductSerializer
from apps.products.models import Product


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    ordering_fields = [
        "title",
        "created_at",
        "updated_at",
    ]
    ordering = ["-created_at"]
    mediator = get_mediator()

    # @extend_schema(
    #     summary="Create a post",
    # )
    # def create(self, request: Request, *args, **kw) -> Response:
    #     pass


class ProductAPIView:
    pass
