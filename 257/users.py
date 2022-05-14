import string

def get_users(passwd: str) -> dict:
    """Split password output by newline,
    extract user and name (1st and 5th columns),
    strip trailing commas from name,
    replace multiple commas in name with a single space
    return dict of keys = user, values = name.
    """
    user_dict = {}

    for line in passwd.splitlines()[1:]:
        username = line.split(":")[0]
        name = line.split(':/')[0].split(':')[-1]
        if name == '':
            name = 'unknown'
        else:
            name = name.replace(',,,,', ' ')
            name = name.replace(',,,', ' ')
            name = name.strip(' ')
        user_dict[username] = name
    return user_dict


