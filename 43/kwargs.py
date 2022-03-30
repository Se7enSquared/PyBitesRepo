def get_profile(*args, name: str ='julian', profession: str ='programmer') -> str:
    if args:
        raise TypeError()
    return f'{name} is a {profession}'
