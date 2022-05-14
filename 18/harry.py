import os
import urllib.request
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)

def _file_to_list(file):
    with open(file) as f:
        return [x.lower() for x in f.read().split() if x.lower()]

def _filter_list(source_list, filter_out_list):
    return [x for x in source_list if x not in filter_out_list and x != '']

def _remove_special_chars(word_list):
    words = []
    for word in word_list:
        words.append(''.join(e for e in word if e.isalnum()))
    return words

def _process_lists():
    stop_list = _file_to_list(stopwords_file)
    stop_list = _remove_special_chars(stop_list)
    text = _file_to_list(harry_text)
    text = _remove_special_chars(text)

    return (text, stop_list)
    

def get_harry_most_common_word():
    text, stop_list = _process_lists()
    filtered_list = _filter_list(text, stop_list)

    count_words = Counter(filtered_list)
    return count_words.most_common(10)[0]
