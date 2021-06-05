from django import test


@test.tag('unit')
@test.override_settings(
    INFLUXDB_ORG='testing-org',
    INFLUXDB_URL='http://testing-url',
    INFLUXDB_TOKEN='testing-token',
    INFLUXDB_BUCKET='testing-bucket',
)
class UnitTestCase(test.SimpleTestCase):
    pass
