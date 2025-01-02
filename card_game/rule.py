"""
Constructs the Rule class.

Makes the Rule class that exists as an interface,
not implemented directly
"""

from typing import List
from card_game.player import Player


class Rule:
    """
    Class to make an abstract Rule lass.
    """

    def deal(self, players: List[Player], cards: List[tuple[str, int]]) -> None:
        """
        Deals in the game
        """
        raise NotImplementedError

    def end_of_hand(
        self, cards: List[tuple[str, int]], players: List[Player]
    ) -> bool:
        """
        Return boolean to indicate if a player has won a hand
        """
        raise NotImplementedError

    def end_of_game(self, players: List[Player]) -> bool:
        """
        Return boolean that indicates multiple hands had been played and the game is over
        """
        raise NotImplementedError

    def turn(self, player: Player, card_drawn: tuple[str, int]) -> None:
        """
        Current player plays a turn
        """
        raise NotImplementedError

    def score(self, players: List[Player]) -> List[int]:
        """
        Calculate and return score for a player
        """
        raise NotImplementedError
