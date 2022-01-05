'''
Word plays
'''

class WordPlayStr(str):
    '''
    A string that can report whether it has interesting properties.
    - abecedarian?
    - palindrome?
    '''
    def same_start_and_end(self):
        ''' (WordPlayStr) -> bool

        Return True if and only if self starts and ends with the same letter.
        The comparison is case-insensitive.

        Precondition: len(self) > 0

        >>> s = WordPlayStr('Abba')
        >>> s.same_start_and_end()
        True
        >>> s = WordPlayStr('canoe')
        >>> s.same_start_and_end()
        False
        '''
        return self[0].lower() == self[-1].lower()


    def is_abecedarian(self, desc=False):
        ''' (WordPlayStr) -> bool

        Return True if self has its letters arranged in alphabetical order and desc is False,
        or if self has its letters arranged in reverse alphabetical order and desc is True.
        The comparison is case-insensitive.

        >>> s = WordPlayStr('almost')
        >>> s.is_abecedarian()
        True
        >>> s = WordPlayStr('Effort')
        >>> s.is_abecedarian()
        True
        >>> s = WordPlayStr('ones')
        >>> s.is_abecedarian()
        False
        >>> s = WordPlayStr('almost')
        >>> s.is_abecedarian(desc=True)
        False
        >>> s = WordPlayStr('one')
        >>> s.is_abecedarian(desc=True)
        True
        '''
        char_list = list(self.lower())
        char_list.sort(reverse=desc)
        return self.lower() == ''.join((char_list))


    def is_palindrome(self):
        ''' (WordPlayStr) -> bool

        Return True if and only if self is a palindrome.
        The comparison is case-insensitive.

        >>> s = WordPlayStr('noon')
        >>> s.is_palindrome()
        True
        >>> s = WordPlayStr('racecar')
        >>> s.is_palindrome()
        True
        >>> s = WordPlayStr('dented')
        >>> s.is_palindrome()
        False
        '''
        char_list = list(self.lower())
        char_list.reverse()
        return self.lower() == ''.join((char_list))


def is_anagram(word1, word2):
    ''' (str, str) -> bool

    Return True if and only if word1 is an anagram of word2.
    The comparison is case-insensitive.

    >>> is_anagram("silent", "listen")
    True
    >>> is_anagram("bear", "breach")
    False
    '''
    char_list1 = list(word1.lower())
    char_list2 = list(word2.lower())

    char_list1.sort()
    char_list2.sort()

    return char_list1 == char_list2
