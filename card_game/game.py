"""
Constructs the Game class.

Makes the Game class
"""

from typing import Optional, List

from card_game.rule import Rule
from card_game.card import Deck
from card_game.player import Player


class Game:
    """
    Class to make a game out of cards.
    """

    def __init__(
        self,
        rule: type[Rule],
        deck: type[Deck],
        num_players: int,
        cards_on_table: Optional[List[tuple[str, int]]] = None,
    ) -> None:
        self.rule = rule
        self.deck = deck
        self.players = list(Player() for _ in range(len(num_players)))
        # should cards_on_table be an attribute of Game or a part of Rule
        if cards_on_table is None:
            self.cards_on_table = cards_on_table
        else:
            cards_on_table = self.cards_on_table

    def __repr__(self) -> str:
        return f"Game(rule='{self.rule}', deck='{self.deck}', players='{self.players}',
        cards_on_table='{self.cards_on_table})"

    def play_a_hand(self) -> None:
        """
        Play a hand, the hand ends when a player wins or when there are
        no more available cards.
        """
        self.rule().deal()
        current_player = 0
        while current_player < len(self.players) and (not self.rule().end_of_hand()):
            self.rule().turn(self.players[current_player])
            current_player += 1
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
