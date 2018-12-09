from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from rest_framework_simplejwt.utils import aware_utcnow
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken


class LogoutView(GenericAPIView, JWTAuthentication):

    def post(self, request):
        if 'refresh' not in request.data:
            return Response(
                data={
                    "refresh": [
                        "This field is required."
                    ]
                }, status=status.HTTP_400_BAD_REQUEST
            )

        login_user = self.authenticate(request)[0]
        OutstandingToken.objects.filter(
            expires_at__lte=aware_utcnow(),
            user=login_user
        ).delete()

        token = RefreshToken(request.data['refresh'])
        token.blacklist()
        return Response(data={}, status=status.HTTP_200_OK)
