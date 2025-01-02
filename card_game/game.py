"""
Constructs the Game class.

Makes the Game class
"""

from typing import Optional, List
from pprint import pp

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
        # rule is consistent
        self.rule = rule
        self.deck = deck
        # players are consistent through out a game.
        self.players = list(
            Player(cards=[], cards_played=[]) for _ in range(num_players)
        )
        # should cards_on_table be an attribute of Game or a part of Rule
        if cards_on_table is None:
            self.cards_on_table = cards_on_table
        else:
            cards_on_table = self.cards_on_table

    def __repr__(self) -> str:
        return f"Game(rule='{self.rule}', \ndeck='{self.deck}', \
        \nplayers='{self.players}',\ncards_on_table='{self.cards_on_table})"

    def play_a_hand(self) -> None:
        """
        Play a hand, the hand ends when a player wins or when there are
        no more available cards.
        """
        deck = self.deck()
        deck.shuffle()
        cards = deck.cards
        self.rule().deal(players=self.players, cards=cards)
        while not self.rule().end_of_hand(cards=cards, players=self.players):
            for player in self.players:
                pp(f"Player {player} has cards {player.cards}")
                self.rule().turn(player, cards.pop())
        self.rule().score(self.players)

    def play_a_game(self) -> None:
        """
        Play hands consecutively. In Rummy, it would be when 500 points is reached.
        """
        while not self.rule().end_of_game(self.players):
            self.play_a_hand()


if __name__ == "__main__":
    game = Game(rule=Rule, deck=Deck, num_players=3)
    print(game)
    print(game.players)
