from datetime import datetime, timedelta
from itertools import islice

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    born = PYBITES_BORN
    while True:
        yield born + timedelta(days=100)
        born = born + timedelta(days=100)