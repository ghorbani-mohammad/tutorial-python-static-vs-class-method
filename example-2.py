from pytz import timezone
from datetime import datetime


class Date(object):
    def __init__(self, datetime):
        self.datetime = datetime

    @staticmethod
    def is_naive(dt):
        if dt.tzinfo is None:
            return True
        return False


if __name__ == "__main__":
    d1 = datetime.utcnow()
    d2 = d1
    utc = timezone("UTC")
    d1 = utc.localize(d1)

    print(d1)
    print(d2)

    d = Date(d1)
    print(Date.is_naive(d1))
    print(Date.is_naive(d2))
    print(d.is_naive(d1))
    print(d.is_naive(d2))
