"""
Tests the Deck class in cards.py
"""

import pytest
from card_game import card


def test_deck_has_12_cards():
    """
    Tests that the deck has 12 cards when initialized.
    """
    deck = card.Deck()
    assert deck.cards is not None
    assert len(deck.cards) == 12


def test_deck_has_been_shuffle():
    """
    Tests that after shuffling cards in a deck in place, there are still 12 cards.
    """
    deck = card.Deck()
    deck.shuffle()
    assert len(deck.cards) == 12


def test_draw_from_deck():
    """
    Tests that when a card is drawn from the deck, the card is an integer.
    """
    deck = card.Deck()
    next_draw = deck.draw()
    assert isinstance(next_draw, int)


def test_draw_from_empty_deck():
    """
    Tests that if the draw method is called on cards in a Deck, an IndexError is raised.
    """
    deck = card.Deck()
    deck.cards = []
    with pytest.raises(IndexError):
        deck.draw()
