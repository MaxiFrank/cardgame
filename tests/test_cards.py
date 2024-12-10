"""
Tests the Deck class in cards.py
"""

import pytest
from card_game import card
from card_game.game import Game

# why can't I do from card_game import player?
# from card_game.player import Player
from card_game.rule import Rule


def test_deck_has_52_cards():
    """
    Tests that the deck has 53 cards when initialized.
    """
    deck = card.Deck()
    assert deck.cards is not None
    assert len(deck.cards) == 52


def test_deck_has_been_shuffle():
    """
    Tests that after shuffling cards in a deck in place, there are still 53 cards.
    """
    deck = card.Deck()
    pre_shuffled_cards = deck.cards[:]
    deck.shuffle()
    assert len(deck.cards) == 52
    assert set(pre_shuffled_cards) == set(deck.cards)
    assert (pre_shuffled_cards == deck.cards) is False


def test_draw_from_deck():
    """
    Tests that when a card is drawn from the deck, the card is an integer.
    """
    deck = card.Deck()
    next_draw = deck.draw()
    suit = next_draw[0]
    number = next_draw[1]
    assert isinstance(next_draw, tuple)
    assert isinstance(suit, str)
    assert isinstance(number, int)


def test_draw_from_empty_deck():
    """
    Tests that if the draw method is called on cards in a Deck, an IndexError is raised.
    """
    deck = card.Deck()
    deck.cards = []
    with pytest.raises(IndexError):
        deck.draw()


def test_game_has_players():
    """
    Tests that the game has 2 players
    """
    game = Game(rule=Rule, deck=card.Deck, num_players=2)
    assert len(game.players) == 2
