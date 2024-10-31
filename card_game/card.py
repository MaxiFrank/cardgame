"""
Constructs the Deck class.

Makes the Deck class that with shuffle and draw methods.
"""

from random import shuffle
from typing import List


class Deck:
    """
    Class to make a deck of cards with shuffle and draw methods.
    """

    def __init__(self) -> None:
        self.cards: List = list(range(1, 13))

    def __repr__(self) -> str:
        return f"Deck(cards='{self.cards}')"

    def shuffle(self) -> None:
        """
        Shuffles cards in deck in place, returns None.
        """
        shuffle(self.cards)

    def draw(self) -> int:
        """
        Draws a card from deck, throws IndexError is cards in deck is empty.
        """
        try:
            return self.cards.pop()
        except IndexError as e:
            raise IndexError("Deck has no cards") from e
