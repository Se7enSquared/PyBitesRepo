import json
import re

def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    dict_list = []
    for file in files:
        with open(file) as f:
            dict_list.append(json.load(f))
    return dict_list


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    for movie in movies:
        if 'Comedy' in movie['Genre']:
            return movie['Title']
    raise KeyError('Movie Not Found')

def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    max_noms = 0
    max_nom_title = ''
    for movie in movies:
        re_group = re.search(r'(\d+)+ nominations', movie['Awards'])
        nominations = int(re_group[1])
        if nominations >= max_noms:
            max_noms = nominations
            max_nom_title = movie['Title']
    return max_nom_title

def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    max_run = 0
    max_run_title = ''
    for movie in movies:
        runtime = int(movie['Runtime'].split(' ')[0])
        if runtime > max_run:
            max_run = runtime
            max_run_title = movie['Title']
    return max_run_title
