import string

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())

def _char_length(pw: str, low: int, high: int):
    return len(pw) >= low and len(pw) <= high

def _has_digit(pw: str):
    for x in pw:
        if x.isdigit():
            return True
    return False

def _has_2_lower(pw: str):
    count = 0
    for x in pw:
        if x.islower():
            count += 1
        if count == 2:
            return True
    return False

def _has_1_upper(pw: str):
    if pw.islower():
        return False
    return True

def _has_punctuation(pw: str):
    for x in pw:
        if x in PUNCTUATION_CHARS:
            return True
    return False

def _not_used_previously(pw: str):
    return pw not in used_passwords

def validate_password(password):
    validations = []

    validations.append(_char_length(password, low=6, high=12))
    validations.append(_has_digit(password))
    validations.append(_has_2_lower(password))
    validations.append(_has_1_upper(password))
    validations.append(_has_punctuation(password))
    validations.append(_not_used_previously(password))

    for valid in validations:
        if not valid:
            return False

    used_passwords.add(password)
    return True

