import pytz
from time import time
from datetime import datetime


def get_timestamp(seconds_since_epoch: float | None = None) -> str:
    if seconds_since_epoch is None:
        seconds_since_epoch = time()
    return datetime.fromtimestamp(
        seconds_since_epoch,
        tz=pytz.timezone("Asia/Taipei")).strftime('%Y-%m-%dT%H:%M:%S%z')