from src.utils.utils import build_datetimestamp, parse_datetimestamp
from datetime import datetime


def test_parse_timestamp():

    now = datetime.now()
    strfd = build_datetimestamp(now)
    parsed = parse_datetimestamp(strfd)
    
    assert now == parsed