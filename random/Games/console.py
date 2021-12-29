"""
Helper function(s) for CLI-based games.
"""
import os


def clear_console():
    """
    clear the console with cls or clear, depending on what operating system
    the machine is running on.

    >>> clearConsole()
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def convert_level(lvl):
    match lvl.lower():
        case 'easy':
            return 1
        case 'normal':
            return 2
        case 'hard':
            return 3
        case _:
            return 0   # 0 is the default case if x is not found

def get_level():
    validated = False
    while not validated:
        level = input("Set difficulty level (easy, normal, hard): ")
        if level.lower() in ["easy", "normal", "hard"]:
            validated = True
        else:
            print("Difficulty level not recognized, pleased try again.")
    level = convert_level(level)
    return level
