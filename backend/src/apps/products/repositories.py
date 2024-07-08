from abc import ABC

from apps.products.models import Product
from seedwork.repositories import GenericRepository, IGenericRepository


class IProductRepository(ABC, IGenericRepository[Product, int]):
    pass


class ProductRepository(IProductRepository, GenericRepository):
    model_class = Product
