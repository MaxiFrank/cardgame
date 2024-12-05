"""
Constructs the Player class.

Makes the Play class
"""

from typing import Optional, List


class Player:
    """
    Class to make a player for a game, takes arguments:
    cards: cards in a player's hand
    cards_played: cards put down on the table for scoring at the end of a hand
    score: score of the cards on the table
    """

    def __init__(
        self,
        cards: Optional[List[int]] = None,
        cards_played: Optional[List[int]] = None,
        score: int = 0,
    ) -> None:

        if cards is None:
            self.cards = []
        else:
            self.cards = cards

        if cards_played is None:
            self.cards_played = []
        else:
            self.cards_played = self.cards_played

        self.score = score

    def __repr__(self) -> str:
        return f"Player(cards='{self.cards}', cards_played='{self.cards_played}', score='{self.score}')"


if __name__ == "__main__":
    players = Player(3)
    print(players)
