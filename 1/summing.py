def sum_numbers(numbers=None):
    if numbers is not None:
        return sum(numbers)
    else:
        lst_100 = list(range(1, 101))
        return sum(lst_100)