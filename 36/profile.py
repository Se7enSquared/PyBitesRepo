def get_profile(name: str, age: int, *args, **kwargs):
    if not isinstance(age, int):
        raise ValueError('age must be an integer')
    if len(args) > 5:
        raise ValueError('too many sports')
    profile = {'name': name, 'age': age}
    if len(args) == 0:
        args = []
    else:
        args = sorted([*args])
        profile['sports'] = args
    if len(kwargs) == 0:
        kwargs = {}
    else:
        profile['awards'] = kwargs
    return profile
