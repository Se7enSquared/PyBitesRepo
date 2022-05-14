import math
def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
        If up=True (default) round up, else round down.
        Return a new list of rounded values
    """
    if up:
        return [math.ceil(num) for num in transactions]
    return [math.floor(num) for num in transactions]