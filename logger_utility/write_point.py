from influxdb_client import WritePrecision
from influxdb_client.client.influxdb_client_async import InfluxDBClientAsync
from influxdb_client.client.write.point import DEFAULT_WRITE_PRECISION
from influxdb_client.client.write_api import WriteApi
from influxdb_client.client.write_api_async import WriteApiAsync

from logger_utility.rich_point import RichPoint


class WritePoint(RichPoint):
    def __init__(
        self, measurement_name: str, write_api: WriteApi | WriteApiAsync = None
    ):
        self._write_api = write_api

        super().__init__(measurement_name=measurement_name)

    async def write(
        self,
        bucket: str,
        org: str = None,
        write_precision: WritePrecision = DEFAULT_WRITE_PRECISION,
    ):
        if isinstance(self._write_api, WriteApi):
            return self._write_api.write(
                bucket=bucket, org=org, record=self, write_precision=write_precision
            )
        elif isinstance(self._write_api, WriteApiAsync):
            return await self._write_api.write(
                bucket=bucket, org=org, record=self, write_precision=write_precision
            )
        return None

    def copy(self):
        r = super().copy()
        w = WritePoint(r._name, self._write_api)
        w._tags = r._tags
        w._fields = r._fields
        w._time = r._time
        return w
