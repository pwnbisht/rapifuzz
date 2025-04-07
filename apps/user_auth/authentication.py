from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import TokenError

from django.conf import settings

class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        """
        Authenticate the user based on a JWT token in the cookies.
        Returns a two-tuple of `User` and token if valid, otherwise raises an
        exception.
        """
        
        raw_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE'])
        if not raw_token:
            return None  # No token provided, authentication skipped.

        try:
            validated_token = self.get_validated_token(raw_token)
        except TokenError:
            self._raise_authentication_error("Invalid or expired token.")

        return self.get_user(validated_token), validated_token