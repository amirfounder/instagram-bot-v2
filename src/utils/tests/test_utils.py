from src.utils.utils import datetimestamp, parse_datetimestamp
from datetime import datetime


def test_parse_timestamp():

    now = datetime.now()
    strfd = datetimestamp(now)
    parsed = parse_datetimestamp(strfd)
    
    assert now == parsed