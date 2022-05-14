import string
def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    return input_string.translate(str.maketrans('', '', string.punctuation))
