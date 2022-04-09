import datetime as dt
def tomorrow(datet=dt.date(2020, 7, 9)):
    return datet + dt.timedelta(days=1)