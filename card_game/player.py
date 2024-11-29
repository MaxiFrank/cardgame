"""
Constructs the Player class.

Makes the Play class
"""

from typing import Optional


class Player:
    """
    Class to make players for a game, takes arguments:
    num_players: int
    current: Optional[int]
    """

    def __init__(self, num_players: int, current: Optional[int] = None) -> None:
        self.players = list(range(num_players))
        if current is None:
            self.current = 0
        else:
            self.current = current

    def __repr__(self) -> str:
        return f"Player(players='{self.players}', current='{self.current}')"

    def get_next_player(self) -> int:
        """
        Return the index of the next player when the turn is not over
        """
        if self.current < len(self.players):
            self.current += 1
        return self.players[self.current]


if __name__ == "__main__":
    players = Player(3)
    print(players)
