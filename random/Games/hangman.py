from random import randrange
import re
from shared import read_textfile
from console import clear_console

def get_min_letters(lvl):
    """
    >>>
    """
    match str(lvl):
        case '1':      # easy
            return 5
        case '2':      # normal
            return 4
        case '3':      # hard
            return 3


def get_max_letters(lvl):
    """
    >>>
    """
    match str(lvl):
        case '1':      # easy
            return 7
        case '2':      # normal
            return 8
        case '3':      # hard
            return 12


def get_max_turns(lvl):
    """
    >>>
    """
    match str(lvl):
        case '1':      # easy
            return 12
        case '2':      # normal
            return 10
        case '3':      # hard
            return 8


def get_word(min_letters, max_letters,count=False):
    file_content = read_textfile("wordlist_nl.txt")
    words = list()
    for line in file_content:
        line = line.strip()
        if line.startswith("#"):
            continue
        elif len(line) >= min_letters and len(line) <= max_letters:
            words.append(line)
    if count:
        return len(words)
    else:
        random_nbr = randrange(0, len(words))
        word = words[random_nbr]
        return word


def play_hangman(level):

    min_letters = get_min_letters(level)
    max_letters = get_max_letters(level)
    turns = get_max_turns(level)

    word = get_word(min_letters, max_letters)
    word_count = get_word(min_letters, max_letters, count=True)
    word = word.lower()
    guesses = ""
    
    prt_txt = (
        f"[SETTINGS] turns: {turns}, word length: {min_letters}-{max_letters}, "
        f"words in database: {word_count}."
    )
    print(prt_txt)

    while True:
        if len(guesses) > 0:
            regex = f"[^{guesses}]"
            hidden = re.sub(regex, "_", word)
        else:
            hidden = "_" * len(word)
        display = list(hidden)
        display = " ".join(display)
        print(display)
        if level == 1 and len(guesses) > 0:
            prt_txt = f"Already tried: {', '.join(guesses)}"
            print(prt_txt)
        guess = input("guess a character: ")
        print(f">{guess}<")
        guess = guess.lower()
        print(f">{guess}<")
        regex = "^[a-z]$"
        if not re.match(regex, guess):
            print("Invalid input. Please enter a single alphabetical character.")
            continue
        clear_console()
        if guess in guesses:
            if level == 1:
                print(f"You've already tried the '{guess}' before. Try again!")
                continue
            elif level == 2:
                print(f"You've already tried the '{guess}' before...")
            elif level == 3:
                pass
        else:
            guesses += guess

        if guess not in word:
            turns -= 1
            if turns == 0:
                prt_txt = f"GAME OVER. The word was '{word}'."
                print(prt_txt)
                break
            print(f"wrong guess. You have {turns} more guesses.")
        else:
            regex = f"[{guesses}]"
            if len(re.findall(regex, word)) == len(word):
                print(word)
                print("You won!!!")
                break
