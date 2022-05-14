def is_armstrong(n: int) -> bool:
    str_num = str(n)
    num_length = len(str_num)
    powered_digits = []
    for digit in str_num:
        powered_digits.append(int(digit)**num_length)

    return sum(powered_digits) == n