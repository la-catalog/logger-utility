import json

from influxdb_client import Point
from rich.console import Console
from rich.json import JSON


class RichPoint(Point):
    def print(self, *args, **kwargs):
        """Print Point as dictionary."""

        Console(*args, **kwargs).log(self.__dict__())
        return self

    def print_json(self, *args, **kwargs):
        """Pretty print Point as JSON (recommended when Point is big)."""

        Console(*args, **kwargs).log(JSON(json.dumps(self.__dict__())))
        return self

    def copy(self):
        p = Point.from_dict(self.__dict__())
        r = RichPoint(p._name)
        r._tags = p._tags
        r._fields = p._fields
        r._time = p._time
        r._write_precision = p._write_precision
        return r

    def __dict__(self) -> dict:
        return {
            "measurement": self._name,
            "tags": self._tags,
            "fields": self._fields,
            "time": self._time,
        }
