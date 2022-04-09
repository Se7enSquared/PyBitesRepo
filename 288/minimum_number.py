from typing import List


def minimum_number(digits: List[int]) -> int:
    if len(digits) == 0: return 0
    unique_digits = sorted(set(digits))
    numstring = ''.join([str(x) for x in unique_digits if str(x) != ''])
    return int(numstring)
