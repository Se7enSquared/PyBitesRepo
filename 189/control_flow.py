IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    filtered_list = []
    for name in names:
        if name.startswith(QUIT_CHAR):
            break
        if len(filtered_list) < MAX_NAMES:
            if not name.startswith(IGNORE_CHAR):
                if not _has_digit(name):
                    filtered_list.append(name)
    return filtered_list

def _has_digit(name):
    has_digit = False
    for char in name:
        if char.isdigit():
            has_digit = True
    return has_digit