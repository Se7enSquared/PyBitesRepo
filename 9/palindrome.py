"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
import os
import urllib.request
import string

TMP = os.getenv("TMP", "/tmp")
DICTIONARY = os.path.join(TMP, "dictionary_m_words.txt")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/dictionary_m_words.txt", DICTIONARY
)


def load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())


def is_palindrome(word):
    """Return if word is palindrome, 'madam' would be one.
    Case insensitive, so Madam is valid too.
    It should work for phrases too so strip all but alphanumeric chars.
    So "No 'x' in 'Nixon'" should pass (see tests for more)"""

    word = word.translate(str.maketrans('', '', string.punctuation)).strip().replace('’', '').lower().replace(' ', '')

    return word == word[::-1]


def get_longest_palindrome(words=None):
    """Given a list of words return the longest palindrome
    If called without argument use the load_dictionary helper
    to populate the words list"""
    if words is None:
        words = load_dictionary()
    max_len = 0
    max_word = ""
    for word in words:
        if is_palindrome(word):
            word_length = len(word)
            if word_length > max_len:
                max_len, max_word = word_length, word
    return max_word
