import os
from collections import Counter
import urllib.request
import xml.etree.ElementTree as ET

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, "feed")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/feed", tempfile
)

with open(tempfile) as f:
    content = f.read().lower()


def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
    data already loaded into the content variable"""
    root = ET.fromstring(content)
    cat_list = []
    for item in root[0].findall('item'):
        for category in item.findall('category'):
            cat_list.append(category.text)
    tag_count = Counter(cat_list)
    return tag_count.most_common(n)
