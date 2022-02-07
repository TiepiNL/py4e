import random

def random_letter(seed=None, upper=False):
    ''' ([int], [bool]) -> str

    Return a random letter.

    >>> random_letter(seed=14)
    'd'
    >>> random_letter(seed=17, upper=True)
    'Q'
    '''
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
                'p','q','r','s','t','u','v','w','x','y','z']
    random.seed(seed)
    if upper:
        return random.choice(alphabet).upper()
    else:
        return random.choice(alphabet)


def is_single_letter(string):
    ''' (str) -> bool
    '''
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
                'p','q','r','s','t','u','v','w','x','y','z']
    return string.lower() in alphabet


def get_scenarios(letter, incl_pos):
    ''' (str, bool) -> list

    '''
    # The game has three types of questions:
    # 1) Next letter?
    # 2) Previous letter?
    # 3) position in alphabet?
    scenarios=[1, 2, 3]

    # Remove the position scenario if it's excluded.
    if incl_pos is not True:
        scenarios.remove(3)

    # There's no next letter after the 'z'.
    if letter.lower() == 'z':
        scenarios.remove(1)
    # There's no previous letter before the 'a'.
    if letter.lower() == 'a':
        scenarios.remove(2)

    return scenarios


def get_position_from_letter(letter):
    ''' (str) -> int
    '''
    alphabet = {'a': 1,
                'b': 2,
                'c': 3,
                'd': 4,
                'e': 5,
                'f': 6,
                'g': 7,
                'h': 8,
                'i': 9,
                'j': 10,
                'k': 11,
                'l': 12,
                'm': 13,
                'n': 14,
                'o': 15,
                'p': 16,
                'q': 17,
                'r': 18,
                's': 19,
                't': 20,
                'u': 21,
                'v': 22,
                'w': 23,
                'x': 24,
                'y': 25,
                'z': 26}
    return alphabet[letter]


def get_letter_from_position(position):
    ''' (str) -> int
    '''
    alphabet = {1: 'a',
                2: 'b',
                3: 'c',
                4: 'd',
                5: 'e',
                6: 'f',
                7: 'g',
                8: 'h',
                9: 'i',
                10: 'j',
                11: 'k',
                12: 'l',
                13: 'm',
                14: 'n',
                15: 'o',
                16: 'p',
                17: 'q',
                18: 'r',
                19: 's',
                20: 't',
                21: 'u',
                22: 'v',
                23: 'w',
                24: 'x',
                25: 'y',
                26: 'z'}
    return alphabet[position]


def get_random_positive_feedback():
    ''' () -> str
    '''
    feedback = ["Well done",
                "Great job!",
                "You rock!",
                "Correct!",
                "Yesss!",
                "That's right!"]
    return random.choice(feedback)


def get_random_negative_feedback():
    ''' () -> str
    '''
    feedback = ["Oops...",
                "Incorrect...",
                "Nope...",
                "That's not right..."]
    return random.choice(feedback)


def practice(incl_pos=True):
    ''' ([bool]) -> NoneType
    '''
    letter = random_letter()
    letter_position = get_position_from_letter(letter)
    scenarios = get_scenarios(letter, incl_pos)
    scenario = random.choice(scenarios)

    if scenario == 1:
        question = f"Which letter comes after the letter '{letter}'? "
    elif scenario == 2:
        question = f"Which letter comes before the letter '{letter}'? "
    elif scenario == 3:
        question = f"What's the position of the letter {letter}'? "

    answer = input(question)
    if scenario != 3 and is_single_letter(answer) is not True:
        quit(1)

    if scenario == 1:
        expected_answer = get_letter_from_position(letter_position + 1)
        explanation = f"After the '{letter}' comes the letter '{expected_answer}'."
    elif scenario == 2:
        expected_answer = get_letter_from_position(letter_position - 1)
        explanation = f"Before the '{letter}' comes the letter '{expected_answer}'."
    elif scenario == 3:
        expected_answer = str(letter_position)
        explanation = f"The position of the letter '{letter}' is {expected_answer}."

    if answer.lower() == expected_answer:
        prefix = get_random_positive_feedback()
    else:
        prefix = get_random_negative_feedback()
    print(f"{prefix} {explanation}")

practice()




if __name__ == '__main__':
    import doctest
    doctest.testmod()
