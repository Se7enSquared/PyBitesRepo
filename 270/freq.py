from collections import defaultdict
def freq_digit(num: int) -> int:
    counter = defaultdict(int)

    for digit in str(num):
        counter[digit] += 1

    max_value = max(counter, key=counter.get)
    return int(max_value)

