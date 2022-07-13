from collections import namedtuple

SUITS = "Red Green Yellow Blue".split()

UnoCard = namedtuple("UnoCard", "suit name")


def create_uno_deck():
    """Create a deck of 108 Uno cards.
    Return a list of UnoCard namedtuples
    (for cards w/o suit use None in the namedtuple)"""

    uno_deck = []

    for suit in SUITS:
        uno_deck.append(UnoCard(suit, "0"))

        for i in range(1, 10):
            uno_deck.extend((UnoCard(suit, str(i)), UnoCard(suit, str(i))))
        for _ in range(2):
            uno_deck.extend(
                (
                    UnoCard(suit, "Draw Two"),
                    UnoCard(suit, "Skip"),
                    UnoCard(suit, "Reverse"),
                )
            )

    for _ in range(4):
        uno_deck.extend((UnoCard(None, "Wild"), UnoCard(None, "Wild Draw Four")))
    return uno_deck
