from drf_spectacular.utils import extend_schema
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.base.tasks import debug_task


@extend_schema(tags=["Default"])
class DebugAPIView(APIView):
    @staticmethod
    def get(request: Request, *args) -> Response:
        debug_task.delay()
        return Response({"message": "Hello world"})
