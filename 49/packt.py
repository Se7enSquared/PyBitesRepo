from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

PACKT = "https://bites-data.s3.us-east-2.amazonaws.com/packt.html"
CONTENT = requests.get(PACKT).text

Book = namedtuple("Book", "title description image link")


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, "html.parser")
    title = soup.find("div", class_="dotd-title").text.strip()
    description = (
        soup.find("div", class_="dotd-title").find_next_sibling("div").text.strip()
    )
    link = soup.find(class_="dotd-main-book-image").find("a")["href"]
    image = (
        soup.find(class_="dotd-main-book-image")
        .find("a")
        .find("noscript")
        .find("img")["src"]
    )

    return Book(title, description, image, link)


