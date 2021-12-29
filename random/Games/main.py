from console import get_level
from higherlower import play_higherlower
from hangman import play_hangman


def play_game(game, level):
    play_again = True
    if game == "higherlower":
        while play_again:
            play_higherlower(level)
            more = input("Press enter to play again or type 'stop' to quit. ")
            if more == "stop":
                play_again = False
    elif game == "hangman":
        while play_again:
            play_hangman(level)
            more = input("Press enter to play again or type 'stop' to quit. ")
            if more == "stop":
                play_again = False


print("Game choices: higherlower, hangman")
game = input("What game do you want to play? ")
level = get_level()
play_game(game, level)
