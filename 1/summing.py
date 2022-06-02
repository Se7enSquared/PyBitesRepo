def sum_numbers(numbers=None):
    return sum(numbers) if numbers is not None else sum(list(range(1, 101)))