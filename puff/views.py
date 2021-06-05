from django.http import response
from django.utils import decorators
from rest_framework import viewsets, decorators as drf_decorators, permissions, mixins

from puff import serializers, influx
from user import auth

method_decorator = decorators.method_decorator
action = drf_decorators.action


@drf_decorators.api_view()
def home(request):
    """
    Health check
    """
    return response.JsonResponse({'success': True})


class IndexView(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (auth.TokenAuth,)
    serializer_class = serializers.PuffSerializer

    def list(self, request, *args, **kwargs):
        data = request.GET
        stats = influx.Stats().get_frequencies(
            user_id=request.user.id,
            start='-' + data.get('from_ago', '1d'),
            window=data.get('group_by', '1h'),
        )
        return response.JsonResponse({'frequencies': stats})
