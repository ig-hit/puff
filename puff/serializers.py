from rest_framework import serializers

from puff import influx


class PuffSerializer(serializers.Serializer):
    def save(self, **kwargs):
        request = self.context.get('request')
        influx.Puff().save({'user_id': request.user.id})
