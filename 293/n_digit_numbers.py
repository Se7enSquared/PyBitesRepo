from typing import List, TypeVar

T = TypeVar("T", int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    if n < 1:
        raise ValueError

    converted_nums = []
    neg = False
    for num in numbers:
        if num < 0:
            neg = True

        num = str(num)
        num = num.replace(".", "")
        num = num.replace("-", "")

        difference = n - len(num)

        if neg:
            num = f'-{num}'

        multiplier = "1"
        if num == 0 or difference == 0:
            converted_nums.append(int(num))
        elif difference < 0:
            multiplier += "0" * abs(n)
            converted_nums.append(int(float(num) / int(multiplier)))
        else:
            multiplier += "0" * (n-1)
            converted_nums.append(int(float(num) * int(multiplier)))

    return converted_nums


print(n_digit_numbers([5.2, 1600, 520, 3600, 13, 55, 4000], 2))
