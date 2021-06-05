from typing import Dict

import influxdb_client
from django.conf import settings

from influx import client


class Puff(client.Client):
    measurement = 'puffs'

    def save(self, item: Dict):
        return super().write(
            influxdb_client.Point.from_dict(
                {
                    'measurement': self.measurement,
                    'tags': {
                        'user_id': item.get('user_id'),
                    },
                    'fields': {
                        'value': 1.0,
                    },
                }
            )
        )


class Stats(client.Client):
    measurement = 'puffs'

    def get_frequencies(self, user_id: str, start: str, window: str):
        query = (
            f'from(bucket: "{settings.INFLUXDB_BUCKET}")'
            f'|> range(start: {start}, stop: now())'
            f'|> filter(fn: (r) => r._measurement == "{self.measurement}" and r.user_id == "{user_id}")'
            f'|> aggregateWindow(every: {window}, fn: count)'
        )
        res = self.read(query)
        if not res:
            return None

        freq = []
        time_format = '%Y-%d-%mT%H:%M:%S'
        for r in res[0].records:
            val = r.values
            freq.append(
                {
                    'from': val.get('_start').strftime(time_format),
                    'to': val.get('_stop').strftime(time_format),
                    'total': val.get('_value'),
                }
            )

        return freq
