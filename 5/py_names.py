NAMES = [
    "arnold schwarzenegger",
    "alec baldwin",
    "bob belderbos",
    "julian sequeira",
    "sandra bullock",
    "keanu reeves",
    "julbob pybites",
    "bob belderbos",
    "julian sequeira",
    "al pacino",
    "brad pitt",
    "matt damon",
    "brad pitt",
]


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
    each name appears only once"""
    new_names = []
    for name in names:
        if name.title() not in new_names:
            new_names.append(name.title())
    return new_names


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    names.sort(key=lambda s: s.split()[1], reverse=True)
    return names


def shortest_first_name(names):
    """Returns the shortest first name (str).
    You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    lowest_len = 100
    shortest_name = ""
    for name in names:
        first_name = name.split(" ")[0]
        if len(first_name) < lowest_len:
            lowest_len = len(first_name)
            shortest_name = first_name
    return shortest_name


print(sort_by_surname_desc(NAMES))
