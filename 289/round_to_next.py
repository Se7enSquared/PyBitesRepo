from re import M


def round_to_next(number: int, multiple: int):
    for i in range(abs(number)):
        if number < 0:
            i = -i
        multiplied = multiple * i

        if number <= multiplied:
            return multiplied

print(round_to_next(-6, -10))