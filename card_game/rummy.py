"""
Constructs the Rummy class, a subclass of Rule

Makes the Rummy class
"""

from typing import List
from card_game.rule import Rule
from card_game.player import Player


class Rummy(Rule):
    """
    Rules:
    player gets dealt cards
    player draws card: add a card
    player plays a turn: 1) pick up cards from where I want to pick up, use that card
    in their play, then discard a card
    """

    def deal(
        self, players: List[type[Player]], cards: List[tuple[str, int]]
    ) -> None:
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

    def end_of_hand(
        self, cards: List[tuple[str, int]], players: List[type[Player]]
    ) -> bool:
        """
        Returns true if a player has won a hand
        A player has won when there's no more available cards
        or when a player has no cards in their hands after a turn
        """
        # players_cards = (len(player.cards) for player in players)
        if (len(cards) == 0) or (
            # next(players_cards)== 0, why is a generator better?
            not all([len(player.cards) for player in players])
        ):
            return True
        return False

    def end_of_game(self, players: List[type[Player]]) -> bool:
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
        same_numbers: dict[int, List[str]] = {}
        for card in player.cards:
            if card[1] in same_numbers:
                same_numbers[card[1]].append(card[0])
            else:
                same_numbers[card[1]] = [card[0]]
        for num, suits in same_numbers.items():
            if len(suits) >= 3:
                for suit in suits:
                    cards_to_put_down.append((suit, num))

    def is_sequential(self, nums: List[int]) -> bool:
        """
        Check if a list of numbers is sequential
        """
        nums.sort()
        prev_idx = 0
        next_idx = 1
        while next_idx < len(nums):
            if nums[next_idx] - nums[prev_idx] != 1:
                return False
            prev_idx = next_idx
            next_idx += 1
        return True

    def set(self, cards: List[tuple[str, int]]) -> bool:
        """
        A set of 3 or more cards of the same rank
        """
        numbers = [card[1] for card in cards]
        return (len(set(numbers)) == 1) and len(cards) >= 3

    def run(self, cards: List[tuple[str, int]]) -> bool:
        """
        A set of three or more sequential cards of the same suit
        """
        suits = [card[0] for card in cards]
        print(suits)
        ranks = [int(card[1]) for card in cards]

        return (
            (self.is_sequential(ranks))
            and (len(set(suits)) == 1)
            and (len(cards) >= 3)
        )

    def parse_tuple_string(self, string: str) -> tuple[str, str]:
        """
        Parse tuple that represents a card, return the suit: str and card: str
        """
        suit = ""
        rank = ""
        for char in string:
            if char.isalpha():
                suit += char
            elif char.isnumeric():
                rank += str(char)
            continue
        return suit, rank

    def turn(self, player: type[Player], card_drawn: tuple[str, int]) -> None:
        """
        player plays a turn:
        1) pick up cards from where the player wants to pick up,
        use that card in their play, then discard a card
        2) player draws a card from the deck of available cards

        Now just need to get the player to answer the questions. If I just run this method,
        that should prompt the user to do something

        also should I break down the discard card and so the logic doesn't get too weird?
        """
        # TODO: do scenario 1

        # Notes for scenario 2
        # when the player takes a turn, if they want to play certain cards, namely put them down in
        #  the player.cards_played
        # This function will either let them do it or not.
        # Regardless of whether a player puts cards down for scoring later, the player needs to
        # put a card into the discard pile

        # player draws a card first
        player.cards.append(card_drawn)

        # Check if the player wants to put any cards down in the cards_played pile so it can
        # be added to score later
        put_cards_down = input("Do you want to put down any cards?\n")
        if put_cards_down == "yes":
            cards_to_put_down = input("What cards do you want to put down?\n")
            if self.run(cards=cards_to_put_down) or self.set(
                cards=cards_to_put_down
            ):
                player.cards_played.extend(cards_to_put_down)
                remaining_cards = [
                    card
                    for card in player.cards
                    if card not in cards_to_put_down
                ]
                player.cards = remaining_cards

        # Mandatory to remove a card from the cards in a player's hand
        card_to_discard = input("What card will you discard?\n")
        suit, rank = self.parse_tuple_string(card_to_discard)
        try:
            player.cards.remove(tuple((suit, int(rank))))
        except ValueError as err:
            print(err.args)

    def calculate_card_value(self, cards: List[tuple[str, int]]) -> int:
        "Calculate points for a list of cards"
        total = 0
        for card in cards:
            if card[1] in (1, 11, 12, 13):
                total += 10
            else:
                total += card[1]
        return total

    def score(self, players: List[type[Player]]) -> List[int]:
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
