from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from accounts.models import Account
from accounts.serializers import AccountSerializer


@extend_schema(tags=["Accounts"])
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
