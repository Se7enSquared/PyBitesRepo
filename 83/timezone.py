from pytz import timezone, utc

AUSTRALIA = timezone("Australia/Sydney")
SPAIN = timezone("Europe/Madrid")


def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
    tuple of Australian and Spanish (timezone aware) datetimes"""
    utc_tz = utc
    aus = utc_tz.localize(naive_utc_dt)
    esp = utc_tz.localize(naive_utc_dt)
    return(aus.astimezone(AUSTRALIA), esp.astimezone(SPAIN))