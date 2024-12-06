from card_game import card, game, rummy
from pprint import pp


if __name__ == "__main__":
    # Get input from the user
    # name = input("Please enter your name: ")
    # print("Hello,", name)
    # play = input("Would you like to play rummy\n")
    # if play == "Yes":
    #     print("let's play")
    # else:
    #     print("next time then")

    num_players = input("how many players are in this game?\n")
    rummy_game = game.Game(
        rule=rummy.Rummy, deck=card.Deck, num_players=int(num_players)
    )
    print("OK lets start")
    # pp(rummy_game.deck().suits)
    # pp(rummy_game.deck().cards)
    # deck = rummy_game.deck()
    # print(len(rummy_game.players))
    # deck.shuffle()
    # pp(rummy_game.players)

    # need to debug play a game...
    rummy_game.play_a_game()
