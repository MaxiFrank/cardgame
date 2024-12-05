"""
Constructs the Rummy class, a subclass of Rule

Makes the Rummy class
"""

from typing import List
from card_game.rule import Rule
from card_game.player import Player
from card_game.card import Deck


class Rummy(Rule):
    """
    Rules:
    player gets dealt cards
    player draws card: add a card
    player plays a turn: 1) pick up cards from where I want to pick up, use that card
    in their play, then discard a card
    """

    def deal(self, players: type[Player], cards: List[tuple[str, int]]) -> None:
        """
        Deal 13 cards per player. Limit to 13 cards.
        """
        for player in players:
            card_dealt = cards.pop(0)
            player.cards.append(card_dealt)

    def end_of_hand(self, deck: type[Deck], players: type[Player]) -> bool:
        """
        Returns true if a player has won a hand
        A player has won when there's no more available cards
        or when a player has no cards in their hands after a turn
        """
        if len(deck.cards) == 0 or not all([len(player.cards) for player in players]):
            return True

    def end_of_game(self, players: type[Player]) -> bool:
        """
        Returns true if a play has won a game
        Game is won when any player gets 500 or more points
        """
        for player in players:
            if player.score >= 500:
                return True
        return False

    def put_down_cards(self, player: type[Player]):
        """
        Player can put down cards that are qualified. The qualified cards are:
        same number but different suit
        same suit but consecutive number
        """
        # TODO: ignore other scenarios for now
        cards_to_put_down = []
        same_numbers = {}
        for card in player.cards:
            if card[1] in same_numbers:
                same_numbers[card[1]].append(card[0])
            else:
                same_numbers[card[1]] = [card[0]]
        for num, suits in same_numbers.items():
            if len(suits) >= 3:
                for suit in suits:
                    cards_to_put_down.append((suit, num))

    def turn(self, player: type[Player], card_drawn: tuple[str, int]) -> None:
        """
        player plays a turn:
        1) pick up cards from where the player wants to pick up,
        use that card in their play, then discard a card
        2) player draws a card from the deck of available cards

        """
        # TODO: do scenario 1
        player.cards.append(card_drawn)

        # loop waiting for players to put down cards.
        # if self.put_down_cards(cards):
        #     player.cards.pop()

    def calculate_card_value(self, cards: List[str, int]) -> int:
        "Calculate points for a list of cards"
        total = 0
        for card in cards:
            if card[1] in (1, 11, 12, 13):
                total += 10
            else:
                total += card[1]
        return total

    def score(self, players: type[Player]) -> List[int]:
        """
        Note this scores for all players.

        Returns the score of a player, get points for cards played (need to track cards played)
        subtract points from cards still in hand (need to track cards in hand)

        if 2 - 10: face points
        if 1, 11, 12, or 13: 10 points
        """
        scores = []
        for player in players:
            points_lost = self.calculate_card_value(player.cards)
            points_gained = self.calculate_card_value(player.cards_played)
            scores.append(points_gained - points_lost)
        return scores
