"""
A3 Problem Domain: Word Search Game

For A3, you will implement a word search game. The game involves a rectangular board
of uppercase letters that is read from a file.

The game also involves a non-empty words list read from a file.

To make it a bit more challenging, there may be words in the words list that do not appear
in the board, and the word list is not shown to the players.

The object of the game is for the players to view the board and find words (remember that the
words list isunknown to the players). Words may be contained in rows (from left to right) or
columns (from top to bottom), but not backwards. When a player correctly guesses a word that
occurs in the words list, that player is awarded points according to a scoring system described
in the starter code. The game ends when all words on the board that appear in the words list have
been guessed.

The player with the highest score wins.

The words from the words list and the letters of the board are made up of alphabetic,
uppercase characters.

Representing a board and a words list in Python
A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']

Functions:
is_valid_word:
checks whether a word that player guessed is in the words list.

make_str_from_row:
creates a string from the list of single character strings representing a row.
Hint: look at how this is used by board_contains_word_in_row.

make_str_from_column:
creates a string from the list of single character strings representing a column.
Hint: this may be helpful for board_contains_word_in_column.

board_contains_word_in_row:
checks whether a word occurs in any of the rows of the board.
This function has been implemented in the starter code.

board_contains_word_in_column:
checks whether a word occurs in any of the columns of the board.
Hint: see board_contains_word_in_row.

board_contains_word:
checks whether a word occurs in any of the rows or columns of the board.

word_score:
calculates the score that a correctly guessed word earns. A word that is only 1 or 2
letters long earns 0 points, a word that is 3-6 letters long earns 1 point per letter,
a word that is 7-9 letters long earns 2 points per letter, and a word that is 10 or
more letters long earns 3 points per letter.

update_score:
adds the score that a correctly guessed word earns to a player's score.

num_words_on_board:
counts how many words from the words list appear on a particular board.

read_words:
creates a words list made up of the words from a file.
Hint: to test this function, you should open a file such as wordslist1.txt
and pass the open file as an argument to this function. See a3_driver.py for an example of this.

read_board:
creates a board made up of the rows of letters from a file.
Hint: to test this function, you should open a file such as board1.txt
and pass the open file as an argument to this function. See a3_driver.py for an example of this.
"""

def is_valid_word(wordlist, word):
    """ (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'OT')
    False
    """
    return word in wordlist


def make_str_from_row(board, row_index):
    """ (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    Precondition: row_index < len(board)

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'XSOB'
    >>> make_str_from_row([['A', 'N', 'T', 'T', 'X', 'S', 'O', 'B']], 0)
    'ANTTXSOB'
    """
    return ''.join(board[row_index])


def make_str_from_column(board, column_index):
    """ (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    Precondition: column_index < len(board[0]),
                  len(board[0]) == len(board[n])

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B'], ['B', 'G', 'E', 'I']], 2)
    'TOE'
    """
    column = ''
    for row in board:
        column += row[column_index]
    return column


def board_contains_word_in_row(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'XOB')
    False
    """

    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True
    return False


def board_contains_word_in_column(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A', 'T', 'N', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    True
    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    """
    for column_index in range(len(board[0])):
        if word in make_str_from_column(board, column_index):
            return True
    return False


def board_contains_word(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'PAN')
    False
    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    >>> board_contains_word([['A', 'T', 'N', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    True
    """
    return board_contains_word_in_row(board, word) or board_contains_word_in_column(board, word)


def word_score(word):
    """ (str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character for all characters in word
                 7-9: 2 points per character for all characters in word
                 10+: 3 points per character for all characters in word

    >>> word_score('AN')
    0
    >>> word_score('PAN')
    3
    >>> word_score('SIXSIX')
    6
    >>> word_score('FORTEEN')
    14
    >>> word_score('EIGHTTEEN')
    18
    >>> word_score('THIRTYPNTS')
    30
    """
    if len(word) >= 10:
        multiplier = 3
    elif len(word) >= 7:
        multiplier = 2
    elif len(word) >= 3:
        multiplier = 1
    else:
        return 0
    return len(word) * multiplier


def update_score(player_info, word):
    """ ([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    """
    new_score = player_info[1] + word_score(word)
    player_info[1] = new_score


def num_words_on_board(board, words):
    """ (list of list of str, list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'],
                            ['X', 'S', 'O', 'B']],
                            ['ANT', 'BOX', 'SOB', 'TO'])
    3
    """
    words_found = 0
    for word in words:
        if board_contains_word(board, word):
            words_found += 1
    return words_found


def read_words(words_file):
    """ (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.

    >>> read_words('wordslist1.txt')
    ['CRUNCHY', 'COWS', 'EAT', 'GRASS']
    """
    word_list = []
    for line in words_file.readlines():
        word_list.append(line.rstrip())
    return word_list


def read_board(board_file):
    """ (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    >>> read_board('board1.txt')
    [['E', 'F', 'J', 'A', 'J', 'C', 'O', 'W', 'S', 'S'],
     ['S', 'D', 'G', 'K', 'S', 'R', 'F', 'D', 'F', 'F'],
     ['A', 'S', 'R', 'J', 'D', 'U', 'S', 'K', 'L', 'K'],
     ['H', 'E', 'A', 'N', 'D', 'N', 'D', 'J', 'W', 'A'],
     ['A', 'N', 'S', 'D', 'N', 'C', 'N', 'E', 'O', 'P'],
     ['P', 'M', 'S', 'N', 'F', 'H', 'H', 'E', 'J', 'E'],
     ['J', 'E', 'P', 'Q', 'L', 'Y', 'N', 'X', 'D', 'L']
     ]
    """
    row_list = []
    for row in board_file.readlines():
        row_list.append(list(row.rstrip()))
    return row_list
