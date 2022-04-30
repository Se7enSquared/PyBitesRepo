from ast import Div
from decimal import DivisionByZero


def positive_divide(numerator, denominator):
    try:
        answer = numerator / denominator
        if answer < 0:
            raise ValueError
        if numerator > 0 and denominator < 0 or numerator < 0 and denominator > 0:
            raise ValueError
        if type(numerator) not in (int, float) or type(denominator) not in (int, float):
            raise TypeError
        return answer
    except ZeroDivisionError:
        return 0
