from random import randrange
import re

words = ["secret", "christmas", "present", "winter"]
random_nbr = randrange(0, len(words))
word = words[random_nbr]
#print(word)

name = input("What's your name? ")
print(f"Hello {name}, it's time to play hangman!")
print("Start guessing...")

turns = 10
guesses = ""

while True:
    if len(guesses) > 0:
        regex = f"[^{guesses}]"
        hidden = re.sub(regex, "_", word)
    else:
        hidden = "_" * len(word)
    print(hidden)

    guess = input("guess a character ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("wrong guess")
        print(f"You have {turns} more guesses")
    else:
        regex = f"[{guesses}]"
        if len(re.findall(regex, word)) == len(word):
            print(word)
            print("You won!!!")
            break

    if turns == 0:
        print("GAME OVER")
        break
