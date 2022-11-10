import os
from datetime import datetime
from unittest import IsolatedAsyncioTestCase, main
from unittest.mock import AsyncMock, patch

from influxdb_client.client.influxdb_client_async import InfluxDBClientAsync

from logger_utility import WritePoint


class TestWritePoint(IsolatedAsyncioTestCase):
    # async def test_copy(self) -> None:
    #     client = InfluxDBClientAsync(
    #         url="http://127.0.0.1:8086", token="TOKEN", org="ORG"
    #     )
    #     write_api = client.write_api()
    #     w = WritePoint("test", write_api).tag("foo", 1).field("bar", 2)
    #     c = w.copy().tag("foobar", 3).field("barfoo", 4)

    #     print(w.to_line_protocol())
    #     print(c.to_line_protocol())

    #     assert "test,foo=1 bar=2i" == w.to_line_protocol()
    #     assert "test,foo=1,foobar=3 bar=2i,barfoo=4i" == c.to_line_protocol()

    #     await client.close()

    async def test_async_write(self) -> None:
        client = InfluxDBClientAsync(
            url="http://127.0.0.1:8086", token="TOKEN", org="ORG"
        )

        (
            await WritePoint("test", AsyncMock())
            .tag("foo", 1)
            .field("bar", 2)
            .time(datetime.utcnow())
            .write(bucket="test")
        )

        await client.close()


if __name__ == "__main__":
    main()
