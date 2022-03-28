import string


def get_index_different_char(chars):
    char_list = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
    
    numeric_count = 0
    non_numeric_count = 0
    numeric_char = []
    non_numeric_char = []
    
    for c in chars:
        if str(c) in char_list:
            numeric_count += 1
            numeric_char.append(c)
        else:
            non_numeric_count += 1
            non_numeric_char.append(c)
        # save iterations and break out of the loop if conditions indicate the character was found
        if (non_numeric_count > 0 and numeric_count > 0) and non_numeric_count != numeric_count:
            break
    if numeric_count > non_numeric_count:
        return chars.index(non_numeric_char[0])
    else:
        return chars.index(numeric_char[0])
