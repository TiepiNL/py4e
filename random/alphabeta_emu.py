"""
Stripped version of alphabeta.py, compatible with:
https://www.programiz.com/python-programming/online-compiler/
"""

import re

def test_abc_word(word):
    """
    Test if the letters of a word have an alphabetical order.
    :param word: the string to test.
    :return: True/False
    """
    abc_word = True
    for pos, val in enumerate(word):
        # Skip the last letter of the word.
        if not pos < len(word)-1:
            continue
        # Compare the current letter with the next one.
        if not val <= word[pos+1]:
            abc_word = False
            break
    return abc_word


def get_abc_words(words, sort=True, abc=True, case_sensitive=False):
    """
    Retrieve all words from a string, test the words for "abc",
    and return a list of all abc-words.
    :param words: the string to test.
    :param sort: whether to sort the list of abc-words or not.
    :param abc: test if the letters of a word have an alphabetical order.
    set to 'False' for a reversed test.
    :case_sensitive: whether the abc-test shuld be case sensitive or not.
    :return: list
    """
    word_list = words.split()
    lmatches = list()
    # Remove all non-alphabet chars.
    regex = re.compile('[^a-zA-Z]')
    for word in word_list:
        # Sorting is case sensitive.
        if not case_sensitive:
            word = word.lower()
        word = regex.sub('', word)

        result = test_abc_word(word)
        if (result and abc) or (not result and not abc):
            if word not in lmatches:
                lmatches.append(word)

    if sort:
        lmatches.sort()

    return lmatches


INPUT = "Accent, chloor, chloor, beknopte, floppy, glossy, dikkop"
matched_words = get_abc_words(INPUT)
print(", ".join(matched_words))
