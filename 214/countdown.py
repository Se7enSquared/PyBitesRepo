def countdown():
    """Write a generator that counts from 100 to 1"""
    for i in range(101, 1, -1):
        try:
            yield i - 1
        except StopIteration:
            raise