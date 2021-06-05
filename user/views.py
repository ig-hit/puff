from rest_framework import throttling
from rest_framework_simplejwt import views as jwt_views

from user import serializers


class LoginThrottle(throttling.AnonRateThrottle):
    rate = '100/hour'


class TokenObtainPairView(jwt_views.TokenObtainPairView):
    throttle_classes = (LoginThrottle,)
    serializer_class = serializers.TokenObtainPairSerializer
