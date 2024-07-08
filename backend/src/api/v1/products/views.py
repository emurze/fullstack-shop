from drf_spectacular.utils import extend_schema
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.dependencies import get_mediator
from api.v1.products.filters import ProductFilter
from api.v1.products.serializers import ProductSerializer
from apps.products.models import Product
from apps.products.services import (
    CreateProductCommand,
    DeleteProductCommand,
    UpdateProductCommand,
)


@extend_schema(tags=["Products"])
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

    @extend_schema(
        summary="Create a post",
    )
    def create(self, request: Request, *args, **kw) -> Response:
        data = ProductSerializer(request.data).data
        command = CreateProductCommand(title=data["title"])
        product_id = self.mediator.handle(command)
        return Response({"id": product_id})

    @extend_schema(
        summary="Update a post",
    )
    def update(self, request, *args, **kw) -> Response:
        data = ProductSerializer(request.data).data
        command = UpdateProductCommand(id=kw["pk"], title=data["title"])
        self.mediator.handle(command)
        return Response()

    @extend_schema(
        summary="Destroy a post",
    )
    def destroy(self, request: Request, *args, **kw) -> Response:
        product_id = kw["pk"]
        command = DeleteProductCommand(id=product_id)
        self.mediator.handle(command)
        return Response({"id": product_id})

    @extend_schema(exclude=True)
    def partial_update(self, request, *args, **kw):
        raise MethodNotAllowed("PATCH")
