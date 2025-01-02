"""
Constructs the Player class.

Makes the Play class
"""

from typing import List
from dataclasses import dataclass, field


@dataclass
class Player:
    """
    Class to make a player for a game, takes arguments:
    cards: cards in a player's hand
    cards_played: cards put down on the table for scoring at the end of a hand
    score: score of the cards on the table
    """

    cards: List[tuple[str, int]] = field(default_factory=list)
    cards_played: List[tuple[str, int]] = field(default_factory=list)
    score: int = 0


if __name__ == "__main__":
    players = Player()
    print(players)
