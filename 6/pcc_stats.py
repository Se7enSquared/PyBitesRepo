from collections import Counter, namedtuple
import os
import urllib.request
import re

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, "dirnames")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/dirnames.txt", tempfile
)

IGNORE = "static templates data pybites bbelderbos hobojoe1848".split()

Stats = namedtuple("Stats", "user challenge")


# code


def gen_files(tempfile=tempfile):
    """
    Parse the tempfile passed in, filtering out directory names
    (first column) using the last "is_dir" column.

    Lowercase these directory names and return them as a generator.

    "tempfile" has the following format:
    challenge<int>/file_or_dir<str>,is_dir<bool>

    For example:
    03/rss.xml,False
    03/tags.html,False
    03/Mridubhatnagar,True
    03/aleksandarknezevic,True

    => Here you would return 03/mridubhatnagar (lowercased!)
       followed by 03/aleksandarknezevic
    """
    with open(tempfile, "r") as f:
        directory_data = f.readlines()

    list_of_directories = []

    for line in directory_data:
        is_dir = line.split(",")[1].rstrip("\n")
        dir_value = line.split(",")[0]
        if is_dir == "True":
            list_of_directories.append(dir_value.lower())

    for directory in list_of_directories:
        yield directory


def diehard_pybites(files=None):
    """
    Return a Stats namedtuple (defined above) that contains:
    1. the user that made the most pull requests (ignoring the users in IGNORE), and
    2. a tuple of:
        ("most popular challenge id", "amount of pull requests for that challenge")

    Calling this function on the default dirnames.txt should return:

    Stats(user='clamytoe', challenge=('01', 7))
    """

    if files is None:
        files = list(gen_files())

    challenges, users = [], []

    for item in files:
        challenge, user = item.split("/")

        if user not in IGNORE:
            challenges.append(challenge)
            users.append(user)

    top_user = Counter(users).most_common(1)[0][0]
    popular_challenges = Counter(challenges).most_common(1)[0]

    return Stats(top_user, popular_challenges)
