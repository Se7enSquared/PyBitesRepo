import functools
from typing import Iterable, Set, Any


def intersection(*args: Iterable) -> Set[Any]:
    filtered = filter(lambda x: x is not None, args)
    iter_list = []
    for iter in filtered:
        iter = filter(lambda x: x != "", iter)
        iter_list.append(set(iter))
    return iter_list[0].intersection(*iter_list[1:])


print(
    intersection(
        ("do you like this bite?", "i hope so"), {"o", "i", "h", "e", "s", " "}
    )
)
