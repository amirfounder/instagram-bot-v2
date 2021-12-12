from datetime import datetime


TODAY_FORMAT = r'%Y_%m_%d'
TIMESTAMP_FORMAT = r'%H_%M_%S_%f'


def today(now: datetime=None):
    now = now if now else datetime.now()
    return now.strftime(TODAY_FORMAT)


def timestamp(now: datetime=None):
    now = now if now else datetime.now()
    return now.strftime(TIMESTAMP_FORMAT)