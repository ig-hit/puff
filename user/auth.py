#from django.contrib.auth import models
from rest_framework import exceptions
from rest_framework_simplejwt import (
    authentication as jwt_authentication,
    exceptions as jwt_exceptions,
    settings as jwt_settings,
)
from user import models
from django.contrib.auth import backends


class AppUserAuthenticator(backends.BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return
        if hasattr(request, 'current_app'):
            return

        try:
            user = models.AppUser.objects.get(email=username)
        except models.AppUser.DoesNotExist:
            return None

        if user.check_password(password) and self.can_authenticate(user):
            return user

    def can_authenticate(self, user):
        return user.is_active


class TokenAuth(jwt_authentication.JWTAuthentication):
    def authenticate(self, request):
        result = super().authenticate(request)
        if not result:
            return
        user, _ = result
        return result

    def get_user(self, validated_token):
        try:
            user_id = validated_token[jwt_settings.api_settings.USER_ID_CLAIM]
        except KeyError:
            raise jwt_exceptions.InvalidToken('Token contained no recognizable user identification')

        try:
            user = models.AppUser.objects.get(id=user_id)
        except models.AppUser.DoesNotExist:
            raise exceptions.AuthenticationFailed()

        return user
