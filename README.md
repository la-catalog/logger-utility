# logger-utility
Use esse pacote para lidar com diversas operações comuns em logs.  

# install
`pdm add logger-utility`  

# usage

## WritePoint

### write(bucket, org, write_precision)
Invoca a função `write` da [WriteAPI](https://influxdb-client.readthedocs.io/en/stable/api.html#influxdb_client.WriteApi.write) ou [WriteApiAsync](https://influxdb-client.readthedocs.io/en/stable/api_async.html#influxdb_client.client.write_api_async.WriteApiAsync.write) passando o a si mesmo como `record`.    

```python
from influxdb_client.client.influxdb_client_async import InfluxDBClientAsync

from logger_utility import WritePoint


client = InfluxDBClientAsync(
    url="http://127.0.0.1:8086", token="TOKEN", org="ORG"
)

write_api = client.write_api()

(
    await WritePoint("test", write_api)
    .tag("foo", 1)
    .field("bar", 2)
    .time(datetime.utcnow())
    .write(bucket="test")
)

await client.close()
```