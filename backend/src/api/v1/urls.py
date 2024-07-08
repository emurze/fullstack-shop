from django.urls import path, include


from rest_framework.routers import SimpleRouter

from api.v1.products.views import ProductModelViewSet

main_router = SimpleRouter()
main_router.register(
    prefix="products",
    viewset=ProductModelViewSet,
    basename="products",
)

urlpatterns = [
    path("", include(main_router.urls)),
]
