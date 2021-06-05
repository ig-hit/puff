from unittest import mock

from puff import serializers
from puff.tests import bootstrap


class PuffSerializerTest(bootstrap.UnitTestCase):
    @mock.patch('puff.serializers.PuffSerializer.context')
    @mock.patch('puff.influx.Puff.save')
    def test_save(self, saver, ser_ctx):
        service = serializers.PuffSerializer()
        item = {'user_id': 'u-1'}
        service._validated_data = item
        ser_ctx.get().user.id = 'u-1'

        service.save()

        saver.assert_called_once_with(item)
