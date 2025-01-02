"""
Tests Rummy rules
"""

from card_game.card import Deck

# why can't I do from card_game import player?
from card_game.player import Player
from card_game.rummy import Rummy


def test_card_dealing():
    """
    Test that each player gets 13 cards in Rummy.
    """
    player_1 = Player()
    player_2 = Player()

    deck = Deck()

    rummy = Rummy()
    rummy.deal(players=[player_1, player_2], cards=deck.cards)

    assert len(player_1.cards) == 13
    assert len(player_2.cards) == 13


def test_valid_set():
    """
    Tests that the set has at least three cards of the same rank and different suits.
    """
    cards = [("Spades", 10), ("Clubs", 10), ("Hearts", 10)]
    rummy = Rummy()
    # Comparison 'rummy.set(cards) == True' should be 'rummy.set(cards) is True' if checking for
    # the singleton value True, or 'rummy.set(cards)' if testing for truthiness
    # (singleton-comparison)
    assert rummy.set(cards)


def test_invalid_set_too_few_cards():
    """
    Tests that when there are fewer than three cards, the player
    can't put the cards down for scoring
    """
    cards = [("Spades", 10), ("Clubs", 10)]
    rummy = Rummy()

    assert rummy.set(cards) is False


def test_invalid_set_not_same_rank():
    """
    Tests that when cards are not of the same rank, the player can't
    put down cards for score
    """
    cards = [("Spades", 10), ("Clubs", 10), ("Hearts", 8)]
    rummy = Rummy()

    assert rummy.set(cards) is False


def test_valid_run():
    """
    Tests that three cards of consecutive rank and the same suit constitute
    valid points to put down for scoring
    """
    cards = [("Spades", 7), ("Spades", 8), ("Spades", 9)]
    rummy = Rummy()

    assert rummy.run(cards) is True


def test_invalid_run_too_few_cards():
    """
    Tests that when there are fewer than 3 cards, a player
    can't put down cards of consecutive rank and the same suits
    """
    cards = [("Spades", 7), ("Spades", 8)]
    rummy = Rummy()

    assert rummy.run(cards) is False


def test_invalid_run_not_same_suit():
    """
    Tests that the cards that are of consecutive rank but different
    suits can't be used for scoring
    """
    cards = [("Spades", 7), ("Spades", 8), ("Clubs", 9)]
    rummy = Rummy()

    assert rummy.run(cards) is False


# TODO: need to do a bunch of patches and mocks here so I can test
# player already has a set or a run, player needs the drawn card to have a set or a run, \
# player doesn't have a set or a run even with the card drawn
