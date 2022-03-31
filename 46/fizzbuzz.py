from typing import Union


def fizzbuzz(num: int) -> Union[str, int]:
    if num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return num
