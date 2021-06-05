import dataclasses
from datetime import datetime
from typing import List
from unittest import mock

from puff import influx
from puff.tests import bootstrap


class PuffTest(bootstrap.UnitTestCase):
    @mock.patch('influx.client.Client.write')
    def test_save(self, writer):
        service = influx.Puff()
        item = {'user_id': 'u-1'}

        service.save(item)
        created_point = writer.call_args[0][0]

        self.assertEqual('puffs', created_point._name)
        self.assertEqual({'user_id': 'u-1'}, created_point._tags)
        self.assertEqual({'value': 1.0}, created_point._fields)


class StatsTest(bootstrap.UnitTestCase):
    @mock.patch('puff.influx.Stats.read')
    def test_get_frequencies(self, reader):
        service = influx.Stats()
        user_id = 'u-1'

        reader.return_value = [
            InfluxTable(records=[InfluxRecord({
                '_start': datetime.now(),
                '_stop': datetime.now(),
                '_value': 1.0,
            })])
        ]

        service.get_frequencies(user_id=user_id, window='10s', start='-1h')

        reader.assert_called_once_with(
            f'from(bucket: "testing-bucket")'
            f'|> range(start: -1h, stop: now())'
            f'|> filter(fn: (r) => r._measurement == "puffs" and r.user_id == "{user_id}")'
            f'|> aggregateWindow(every: 10s, fn: count)'
        )


@dataclasses.dataclass
class InfluxRecord(object):
    values: dict


@dataclasses.dataclass
class InfluxTable(object):
    records: List[InfluxRecord]
