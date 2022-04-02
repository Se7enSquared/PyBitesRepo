from ast import Eq
from enum import Enum


class Equality(Enum):
    SAME_REFERENCE = 4
    SAME_ORDERED = 3
    SAME_UNORDERED = 2
    SAME_UNORDERED_DEDUPED = 1
    NO_EQUALITY = 0


def check_equality(list1, list2):
  if list1 is list2:
    return Equality.SAME_REFERENCE
  elif list1 == list2:
    return Equality.SAME_ORDERED
  elif sorted(list1) == sorted(list2):
    return Equality.SAME_UNORDERED
  elif set(sorted(list1)) == set(list2):
    return Equality.SAME_UNORDERED_DEDUPED
  else:
    return Equality.NO_EQUALITY

