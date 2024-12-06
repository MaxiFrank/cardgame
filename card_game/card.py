"""
Constructs the Deck class.

Makes the Deck class that with shuffle and draw methods.
"""

from pprint import pp
from random import shuffle
from typing import List


class Deck:
    """
    Class to make a deck of cards with shuffle and draw methods.
    Cards have 4 suits and 13 ranks.
    """

    def __init__(self) -> None:
        self.suits: List[str] = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards: List[tuple[str, int]] = []
        for suit in self.suits:
            for num in list(range(1, 14)):
                self.cards.append((suit, num))

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


if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    card = deck.draw()
    pp(card)
