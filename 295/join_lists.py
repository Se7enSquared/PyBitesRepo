from typing import List, Union


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    if not lst_of_lst: return None
    new_list = []
    for lst in lst_of_lst:
        new_list.extend(iter(lst))
        new_list.append(sep)
    return new_list[:-1]