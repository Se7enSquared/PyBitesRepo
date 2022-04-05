def find_number_pairs(numbers, N=10):

    numbers_seen = []
    num_list = []

    for number in numbers:
        target_num = round(N - number, 2)
        if (target_num) in numbers_seen:
            num_list.append((target_num, number))
        numbers_seen.append(number)

    return num_list