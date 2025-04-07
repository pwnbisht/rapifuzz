import pytz
import datetime
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

def set_auth_cookies(
    response: Response,
    refresh_token: RefreshToken
) -> None:
    """
    Helper function to set authentication cookies for access and refresh
    tokens, and calculate the max age for the tokens.

    Args:
        response (Response): The response object where cookies will be set.
        refresh_token (RefreshToken): The refresh token object (contains both
        refresh and access tokens).
    """

    access_token = refresh_token.access_token
    access_exp_timestamp = access_token.payload["exp"]
    refresh_exp_timestamp = refresh_token.payload["exp"]
    user_tz = pytz.timezone(settings.TIME_ZONE)
    current_timestamp = datetime.datetime.now(user_tz).timestamp()

    access_max_age = int(access_exp_timestamp - current_timestamp)
    refresh_max_age = int(refresh_exp_timestamp - current_timestamp)

    response.set_cookie(
        key=settings.SIMPLE_JWT["AUTH_COOKIE"],
        value=str(access_token),
        max_age=access_max_age,
        # domain=settings.SIMPLE_JWT["AUTH_COOKIE_DOMAIN"],  # noqa: ERA001
        secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
        httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
        samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
    )

    response.set_cookie(
        key=settings.SIMPLE_JWT["AUTH_COOKIE_REFRESH"],
        value=str(refresh_token),
        max_age=refresh_max_age,
        # domain=settings.SIMPLE_JWT["AUTH_COOKIE_DOMAIN"],  # noqa: ERA001
        secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
        httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
        samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
    )


def delete_auth_cookies(response):
    """
    Helper function to delete authentication cookies.

    Args:
        response (Response): The response object where cookies will be deleted.
    """
    # response.delete_cookie(settings.SIMPLE_JWT["AUTH_COOKIE"])  # noqa: E501, ERA001
    # response.delete_cookie(settings.SIMPLE_JWT["AUTH_COOKIE_REFRESH"])  # noqa: E501, ERA001
    response.delete_cookie(
        settings.SIMPLE_JWT["AUTH_COOKIE"],
        samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
    )
    response.delete_cookie(
        settings.SIMPLE_JWT["AUTH_COOKIE_REFRESH"],
        samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
    )