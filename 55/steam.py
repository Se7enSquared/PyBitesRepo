from collections import namedtuple
import re
from feedparser import parse

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple('Game', 'title link')


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    steam_feed = parse(FEED_URL)
    Game = namedtuple('Game', 'title link')
    games = []
    for entry in steam_feed.entries:
        games.append(Game(entry.title, entry.link))
    return games
    