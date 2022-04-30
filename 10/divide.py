from ast import Div
from decimal import DivisionByZero


def positive_divide(numerator, denominator):
    try:
        answer = numerator / denominator
    except ZeroDivisionError:
        return 0
    except (TypeError, ValueError):
        raise
    else:
        if answer < 0:
            raise ValueError('cannot be negative')
        return answer