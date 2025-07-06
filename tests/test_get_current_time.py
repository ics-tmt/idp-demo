import datetime
import get_current_time


def test_get_current_time_returns_datetime():
    now = get_current_time.get_current_time()
    assert isinstance(now, datetime.datetime)


def test_get_current_time_is_recent():
    now = get_current_time.get_current_time()
    delta = datetime.datetime.now() - now
    assert abs(delta.total_seconds()) < 1