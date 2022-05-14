VOWELS = "aeiou"
PYTHON = "python"


def contains_only_vowels(input_str):
   """Receives input string and checks if all chars are
   VOWELS. Match is case insensitive."""
   unique_chars = set(input_str.lower())
   return len([x for x in unique_chars if x not in VOWELS]) == 0


def contains_any_py_chars(input_str):
   """Receives input string and checks if any of the PYTHON
   chars are in it. Match is case insensitive."""
   return len([x for x in input_str.lower() if x in PYTHON]) > 0


def contains_digits(input_str):
   """Receives input string and checks if it contains
   one or more digits."""
   unique_chars = set(input_str.lower())
   for char in unique_chars:
      if char.isdigit():
         return True
   return False