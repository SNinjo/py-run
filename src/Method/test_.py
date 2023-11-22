import re
from time import time
from datetime import datetime
from freezegun import freeze_time

from Method import get_timestamp


def test_get_timestamp():
    seconds = time()
    assert re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+0800$',
                    get_timestamp(seconds)) is not None
    assert get_timestamp(
        seconds
    ) == f'{datetime.fromtimestamp(seconds).strftime("%Y-%m-%dT%H:%M:%S")}+0800'

    seconds = 1000000000
    assert re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+0800$',
                    get_timestamp(seconds)) is not None
    assert get_timestamp(
        seconds
    ) == f'{datetime.fromtimestamp(seconds).strftime("%Y-%m-%dT%H:%M:%S")}+0800'


class PastTime:

    @staticmethod
    def get_seconds_since_epoch() -> int:
        return 1000000000

    @staticmethod
    def get_time_text() -> str:
        return '2001-09-09 01:46:40'


class FutureTime:

    @staticmethod
    def get_seconds_since_epoch() -> int:
        return 1800000000

    @staticmethod
    def get_time_text() -> str:
        return '2027-01-15 08:00:00'


@freeze_time(PastTime.get_time_text(), tz_offset=8)
def test_get_timestamp_past_time():
    assert get_timestamp(
    ) == f'{datetime.fromtimestamp(PastTime.get_seconds_since_epoch()).strftime("%Y-%m-%dT%H:%M:%S")}+0800'


@freeze_time(FutureTime.get_time_text(), tz_offset=8)
def test_get_timestamp_future_time():
    assert get_timestamp(
    ) == f'{datetime.fromtimestamp(FutureTime.get_seconds_since_epoch()).strftime("%Y-%m-%dT%H:%M:%S")}+0800'