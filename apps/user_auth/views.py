from typing import Any
from rest_framework import generics
from .serializers import UserSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from .serializers import ArtistLoginSerializer
from apps.utils.auth import set_auth_cookies


class UserSignupView(generics.CreateAPIView):
    """
    Handle the POST request for user signup.
    """
    serializer_class = UserSerializer
    permission_classes = []
    

@method_decorator(sensitive_post_parameters("password"), name="dispatch")
class UserLoginView(APIView):
    """
    Handle the POST request for user login.

    Return a JSON response containing the user's refresh token.
    """
    permission_classes = [AllowAny]
    serializer_class = ArtistLoginSerializer
    authentication_classes = []

    def post(
        self, request: Request,
        *args: Any, **kwargs: Any
    ) -> Response:
        """
        Handle the POST request for user login.

        Return a JSON response containing the user's refresh token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = authenticate(request=request, email=email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            resp = Response(
                {
                    "status": "success",
                },
                status=status.HTTP_200_OK,
            )
            set_auth_cookies(resp, refresh)
            return resp

        return Response(
            {"error": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED,
        )
