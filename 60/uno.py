from collections import namedtuple

SUITS = 'Red Green Yellow Blue'.split()

UnoCard = namedtuple('UnoCard', 'suit name')


def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""

    uno_deck = []

    for suit in SUITS:
        uno_deck.append(UnoCard(suit, '0'))
        uno_deck.append(UnoCard(suit, '1'))
        uno_deck.append(UnoCard(suit, '1'))
        uno_deck.append(UnoCard(suit, '2'))
        uno_deck.append(UnoCard(suit, '2'))
        uno_deck.append(UnoCard(suit, '3'))
        uno_deck.append(UnoCard(suit, '3'))
        uno_deck.append(UnoCard(suit, '4'))
        uno_deck.append(UnoCard(suit, '4'))
        uno_deck.append(UnoCard(suit, '5'))
        uno_deck.append(UnoCard(suit, '5'))
        uno_deck.append(UnoCard(suit, '6'))
        uno_deck.append(UnoCard(suit, '6'))
        uno_deck.append(UnoCard(suit, '7'))
        uno_deck.append(UnoCard(suit, '7'))
        uno_deck.append(UnoCard(suit, '8'))
        uno_deck.append(UnoCard(suit, '8'))
        uno_deck.append(UnoCard(suit, '9'))
        uno_deck.append(UnoCard(suit, '9'))
        uno_deck.append(UnoCard(suit, 'Draw Two'))
        uno_deck.append(UnoCard(suit, 'Draw Two'))
        uno_deck.append(UnoCard(suit, 'Skip'))
        uno_deck.append(UnoCard(suit, 'Skip'))
        uno_deck.append(UnoCard(suit, 'Reverse'))
        uno_deck.append(UnoCard(suit, 'Reverse'))

    uno_deck.append(UnoCard(None, 'Wild'))
    uno_deck.append(UnoCard(None, 'Wild'))
    uno_deck.append(UnoCard(None, 'Wild'))
    uno_deck.append(UnoCard(None, 'Wild'))
    uno_deck.append(UnoCard(None, 'Wild Draw Four'))
    uno_deck.append(UnoCard(None, 'Wild Draw Four'))
    uno_deck.append(UnoCard(None, 'Wild Draw Four'))
    uno_deck.append(UnoCard(None, 'Wild Draw Four'))

    return uno_deck
