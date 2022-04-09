from typing import List, Union


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    if len(lst_of_lst) == 0: return None
    new_list = []
    for lst in lst_of_lst:
        for item in lst:
            new_list.append(item)
        new_list.append(sep)
    return new_list[:-1]