import random

names = "Julian Bob PyBites Dante Martin Rodolfo".split()
aliases = "Pythonista Nerd Coder".split() * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = " | "

def generate_table(*args):
    combined_lists = list(zip(*args))
    final_list = []
    for tuples in combined_lists:
        temp_string = "".join(str(item) + SEPARATOR for item in tuples)
        final_list.append(temp_string.strip(" | "))
    return final_list

