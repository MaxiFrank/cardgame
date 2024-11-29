"""
Constructs the Game class.

Makes the Game class
"""

from typing import Optional

from card_game.rule import Rule
from card_game.card import Deck
from card_game.player import Player


class Game:
    """
    Class to make a game out of cards.
    """

    def __init__(self, rule: type[Rule], deck: type[Deck], num_players: int) -> None:
        self.rule = rule
        self.deck = deck
        self.players = Player(num_players)

    def __repr__(self) -> str:
        return f"Game(rule='{self.rule}', deck='{self.deck}', players='{self.players}')"

    def play_a_hand(self) -> None:
        """
        Play until a player wins.
        """
        self.rule().deal()
        current_player: Optional[int] = None
        while not self.rule().end_of_hand():
            self.rule().turn(current_player)
            current_player = self.players.get_next_player()
        self.rule().score()

    def play_a_game(self) -> None:
        """
        Play hands consecutively. In Rummy, it would be when 500 points is reached.
        """
        while not self.rule().end_of_game():
            self.play_a_hand()


if __name__ == "__main__":
    game = Game(rule=Rule, deck=Deck, num_players=3)
    print(game)
    print(game.players)
