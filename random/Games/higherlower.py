import logging as log
import math
from random import randrange
from console import clear_console

def get_max_number(lvl):
    """
    >>>
    """
    match str(lvl):
        case '1':      # easy
            return 10
        case '2':      # normal
            return 100
        case '3':      # hard
            return 100000


def get_max_turns(lvl):
    """
    >>>
    """
    # Use the logarithm method to calculate the amount of turns a computer
    # needs (worst case) for the given range, and set a multiply this
    # with a multiplier based on the level.
    # This way the max turns dynamically adjusts if ranges get changed.
    maxnr = math.log(get_max_number(lvl), 2)
    match str(lvl):
        case '1':      # easy
            multiplier = 2
        case '2':      # normal
            multiplier = 1.3
        case '3':      # hard
            multiplier = 1
    return int(maxnr * multiplier)


def get_computer_score(random_nbr, max_nbr):
    """
    >>>
    """
    # Start with a guess halfway.
    guess = max_nbr // 2
    val_too_high = max_nbr
    val_too_low = 0
    attempts = 0
    while True:
        attempts += 1

        logtxt = f"[{attempts}] target: {random_nbr}, guess: {guess}"
        log.info(logtxt)

        if guess == random_nbr:
            # Found it!
            break
        elif guess > random_nbr:
            val_too_high = guess
            guess -= (guess - val_too_low) // 2
        elif guess < random_nbr:
            val_too_low = guess
            guess += (val_too_high - guess) // 2
    
    return attempts


def play_higherlower(level):
    max_turns = get_max_turns(level)
    max_nbr = get_max_number(level)
    random_nbr = randrange(1, max_nbr + 1)
    turns = 1
    game_over = False
    while True:
        prt_txt = f"Turn {turns} of {max_turns}."
        print(prt_txt)
        user_nbr = input(f"Enter a number between 1 and {max_nbr}: ")
        clear_console()
        if user_nbr in ["stop", "abort", "cancel", "stop", "quit", "exit"]:
            print(f"The secret number was {random_nbr}")
            break
        else:
            try:
                user_nbr = int(user_nbr)
            except ValueError:
                print("ERROR: Please enter a valid number between 1 and 100.")
                continue
        if user_nbr == random_nbr:
            prt_txt = f"You are right, {user_nbr} it is. Great job!"
            print(prt_txt)
            comp_score = get_computer_score(random_nbr, max_nbr)
            if turns < comp_score:
                comp_txt = "You've beaten the computer!"
            elif turns == comp_score:
                comp_txt = "You were as quick as the computer!"
            else:
                comp_txt = "Next time, try the beat the computer!"

            prt_txt = (
                f"The computer solved it in {comp_score} turns, you needed {turns}. {comp_txt}"
            )
            print(prt_txt)
            break

        turns += 1
        if turns > max_turns:
            game_over = True
            whats_next = f"No turns left: GAME OVER. The correct number was {random_nbr}."
        else:
            whats_next = "Try again!"

        if user_nbr < random_nbr:
            lowhigh = "low"
        else:
            lowhigh = "high"
        print(f"your guess of {user_nbr} is too {lowhigh}. {whats_next}")

        if game_over:
            break
