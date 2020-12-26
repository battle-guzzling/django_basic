from rest_framework.views import APIView
from AccountManagement.serializers.requests import SignInRequestSerializer
from drf_yasg.utils import swagger_auto_schema

from Common.views import reponses


class SignInAPI(APIView):
    authentication_classes = []
    permission_classes = []

    @swagger_auto_schema(
        operation_description="Sign in to system via API",
        operation_summary="Sign in to system via API",
        request_body=SignInRequestSerializer,
        responses={200: "Success"},
    )
    def post(self, request, format=None):
        request_data = SignInRequestSerializer(data=request.data)
        request_data.is_valid()

        return reponses.success("Thành công nha", {})
