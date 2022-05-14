from collections import Counter
def major_n_minor(numbers):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """

    c = Counter(numbers)
    return c.most_common(1)[0][0], c.most_common()[:-1-1:-1][0][0]