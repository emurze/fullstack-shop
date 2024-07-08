from django.urls import path, include

from api.v1.products.router import products_router

urlpatterns = [
    path("", include(products_router.urls)),
]
