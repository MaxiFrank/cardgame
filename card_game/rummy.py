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
        dealt_cards = 0
        while dealt_cards < 13:
            for player in players:
                # issue: pop from an empty list, need to check if there's any cards in cards...
                # consider using the end_of_game method
                card_dealt = cards.pop(0)
                player.cards.append(card_dealt)
            dealt_cards += 1

    def end_of_hand(self, cards: List[tuple[str, int]], players: type[Player]) -> bool:
        """
        Returns true if a player has won a hand
        A player has won when there's no more available cards
        or when a player has no cards in their hands after a turn
        """
        if (len(cards) == 0) or (not all([len(player.cards) for player in players])):
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

        # Notes for scenario 2
        # this is where I put in the rules for same number, different suits and same suit, consecutive numbers.
        # when the player takes a turn, if they want to play certain cards, namely put them down in the player.cards_played
        # This function will either let them do it or not.
        # Regardless of whether a player puts cards down for scoring later, the player needs to put a card into the discard pile

        # player draws a card first
        player.cards.append(card_drawn)

    def calculate_card_value(self, cards: List[tuple[str, int]]) -> int:
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
