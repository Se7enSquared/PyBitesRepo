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
    with open(MOVIE_DATA, "r") as f:
        csv_reader = csv.reader(f, delimiter=",")
        # skip the header row
        next(csv_reader)
        for row in csv_reader:
            director = row[1]
            title = row[11].strip("\xa0")
            year = row[23]
            if year == '' or int(year) < MIN_YEAR:
                continue
            score = float(row[25])
            directors[director].append(Movie(title, year, score))
    return directors


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
    round the mean to 1 decimal place"""
    count, sum = len(movies), 0
    for movie in movies:
        sum += movie.score
    return round(sum / count, 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
    return a list of tuples (director, average_score) ordered by highest
    score in descending order. Only take directors into account
    with >= MIN_MOVIES"""
    director_scores = []
    for director, movies  in directors.items():
        if len(movies) >= MIN_MOVIES:
            average_score = calc_mean_score(movies)
            if average_score > 0:
                director_scores.append((director, average_score))
    return sorted(director_scores, key = lambda x: x[1], reverse = True)


