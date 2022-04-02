import string
def count_indents(text: str) -> int:
    """
    Count and return the number of leading white space characters (' ').
    """
    if '\t' in text:
        return 0
    return len(text) - len(text.lstrip())