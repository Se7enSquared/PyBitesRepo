PYBITES = "pybites"


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    new_str = ''
    for char in text:
        if char.lower() in PYBITES:
            new_str += char.swapcase()
        else:
            new_str += char
    return new_str
