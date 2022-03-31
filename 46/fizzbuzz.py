from typing import Union


def fizzbuzz(num: int) -> Union[str, int]:
    if int(num) % 3 == 0:
        print('fizz')
    elif int(num) % 5 == 0:
        print('buzz')
    else:
        print(str(num))
