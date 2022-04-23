import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
S3 = "https://bites-data.s3.us-east-2.amazonaws.com/"
DICT = "dictionary.txt"
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(f"{S3}{DICT}", DICTIONARY)

scrabble_scores = [
    (1, "E A O I N R T L S U"),
    (2, "D G"),
    (3, "B C M P"),
    (4, "F H V W Y"),
    (5, "K"),
    (8, "J X"),
    (10, "Q Z"),
]
LETTER_SCORES = {
    letter: score for score, letters in scrabble_scores for letter in letters.split()
}

# start coding

def load_words():
    """Load the words dictionary (DICTIONARY constant) into a list and return it"""
    with open(DICTIONARY, 'r') as f:
        word_list = [word.rstrip('\n') for word in f.readlines()]
    return word_list


def calc_word_value(word):
    """Given a word calculate its value using the LETTER_SCORES dict"""
    score = 0
    for letter in word:
        for score_tuple in scrabble_scores:
            if letter.upper() in score_tuple[1].split(" "):
                score += score_tuple[0]
                continue
    return score



def max_word_value(words):
    """Given a list of words calculate the word with the maximum value and return it"""
    max_value = 0
    max_word = ''
    for word in words:
        word_value = calc_word_value(word)
        if word_value > max_value:
            max_value = word_value
            max_word = word
    return max_word

