def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    try:
        if fmt.lower() == 'cm':
            result = _convert_inches_to_cm(value)
        elif fmt.lower() == 'in':
            result = _convert_cm_to_inches(value)
        else:
            raise ValueError
        return round(result, 4)
    except TypeError:
        raise


def _convert_inches_to_cm(value):
    return float(value * 2.54)


def _convert_cm_to_inches(value):
    return float(value / 2.54 )
