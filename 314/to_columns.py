from typing import List  # not needed when we upgrade to 3.9


def print_names_to_columns(names: List[str], cols: int = 2) -> None:
    for i in range(0, len(names), cols):
        print(''.join("{:<12}".format('| ' + name) for name in names[i:i + cols]))
