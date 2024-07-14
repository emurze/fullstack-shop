from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView

from pizzas.models import Pizza
from pizzas.serializers import PizzaSerializer


@extend_schema(tags=["Pizzas"])
class PizzaAPIListView(ListAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
