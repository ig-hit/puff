from rest_framework import exceptions
from rest_framework_simplejwt import serializers as jwt_serializers

from user import models


class TokenObtainPairSerializer(jwt_serializers.TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        return self.for_user(self.user, data=data)

    def for_user(self, user, data=None):
        if not isinstance(user, models.AppUser):
            raise exceptions.PermissionDenied()

        if not data:
            data = dict()
        refresh = self.get_token(user)
        access = refresh.access_token

        access['username'] = user.username
        access['first_name'] = user.first_name
        access['last_name'] = user.last_name

        data['refresh'] = str(refresh)
        data['access'] = str(access)

        return data
