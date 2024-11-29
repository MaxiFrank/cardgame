"""
Constructs the Rule class.

Makes the Rule class that exists as an interface,
not implemented directly
"""

from typing import Optional


class Rule:
    """
    Class to make an abstract Rule lass.
    """

    def deal(self) -> None:
        """
        Deals in the game
        """
        raise NotImplementedError

    def end_of_hand(self) -> bool:
        """
        Return boolean to indicate if a player has won a hand
        """
        raise NotImplementedError

    def end_of_game(self) -> bool:
        """
        Return boolean that indicates multiple hands had been played and the game is over
        """
        raise NotImplementedError

    def turn(self, player: Optional[int]) -> None:
        """
        Current player plays a turn
        """
        raise NotImplementedError

    def score(self) -> int:
        """
        Calculate and return score for a player
        """
        raise NotImplementedError
