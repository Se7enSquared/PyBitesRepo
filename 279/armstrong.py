def is_armstrong(n: int) -> bool:
    str_num = str(n)
    num_length = len(str_num)
    powered_digits = [int(digit)**num_length for digit in str_num]
    return sum(powered_digits) == n