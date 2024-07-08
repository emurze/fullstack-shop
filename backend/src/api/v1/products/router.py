from rest_framework.routers import SimpleRouter

from api.v1.products.views import ProductModelViewSet

products_router = SimpleRouter()
products_router.register("products", ProductModelViewSet)
