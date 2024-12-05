from card_game import card, game, rummy
from pprint import pp


if __name__ == "__main__":
    rummy_game = game.Game(rule=rummy.Rummy, deck=card.Deck, num_players=2)
    # pp(rummy_game.deck().suits)
    # pp(rummy_game.deck().cards)
    deck = rummy_game.deck()
    # pp(rummy_game.players)
    deck.shuffle()
    rummy_game.play_a_game()
