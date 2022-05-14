import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

BASE_URL = "https://bites-data.s3.us-east-2.amazonaws.com/"
TMP = os.getenv("TMP", "/tmp")

fname = "movie_metadata.csv"
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple("Movie", "title year score")


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies
    use the defined Movie namedtuple"""
    directors = defaultdict(list)
    print(csv.__file__)
    with open(MOVIE_DATA, "r") as f:
        csv_reader = csv.reader(f, delimiter=",")
        for row in csv_reader:
            directors[row[1]].append(row[11].strip("\xa0"))
    # for k, v in directors.items():
    #     if k == 'Sergio Leone':
    #         print(f'{k}: {v}')
    return directors


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
    round the mean to 1 decimal place"""
    pass


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
    return a list of tuples (director, average_score) ordered by highest
    score in descending order. Only take directors into account
    with >= MIN_MOVIES"""

    # NOTE: I need to figure out how to get the movies scores and the directors together
    # TOO TIRED to keep going :(
    directors = get_movies_by_director()
    scores = defaultdict(list)
    directors_scores = []
    with open(MOVIE_DATA, "r") as f:
        csv_reader = csv.reader(f, delimiter=",")
        for row in csv_reader:
            scores[row[11]].append(row[25])
    merged_dict = directors.update(scores)
    for director, movie in merged_dict.items():
        directors_scores.append(director, scores[movie])
    print(directors_scores)


get_average_scores(get_movies_by_director())
