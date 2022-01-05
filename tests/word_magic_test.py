'''
Unit tests of the WordPlay project code.
'''
import doctest
import unittest
import abc.word_magic as prj


class TestSameStartEndEnd(unittest.TestCase):
    '''unittest test methods for word_magic.'''

    def test_same_start_and_end_1(self):
        '''Test same_start_and_end with a single character.'''
        wp_str = prj.WordPlayStr('a')
        actual = wp_str.same_start_and_end()
        expected = True
        self.assertEqual(expected, actual)

    def test_same_start_and_end_2(self):
        '''Test same_start_and_end with upper/lowercase match.'''
        wp_str = prj.WordPlayStr('Abba')
        actual = wp_str.same_start_and_end()
        expected = True
        self.assertEqual(expected, actual)

    def test_same_start_and_end_3(self):
        '''Test same_start_and_end with no match.'''
        wp_str = prj.WordPlayStr('canoe')
        actual = wp_str.same_start_and_end()
        expected = False
        self.assertEqual(expected, actual)


class TestIsAbecedarian(unittest.TestCase):
    '''unittest test methods for is_abecedarian.'''

    def test_is_abecedarian_1(self):
        '''Test is_abecedarian with an empty string.'''
        wp_str = prj.WordPlayStr('')
        actual = wp_str.is_abecedarian()
        expected = True
        self.assertEqual(expected, actual)

    def test_is_abecedarian_2(self):
        '''Test is_abecedarian with a single character.'''
        wp_str = prj.WordPlayStr('a')
        actual = wp_str.is_abecedarian()
        expected = True
        self.assertEqual(expected, actual)

    def test_is_abecedarian_3(self):
        '''Test is_abecedarian with an abecedarian word.'''
        wp_str = prj.WordPlayStr('almost')
        actual = wp_str.is_abecedarian()
        expected = True
        self.assertEqual(expected, actual)

    def test_is_abecedarian_4(self):
        '''Test is_abecedarian with a capitalized abecedarian word.'''
        wp_str = prj.WordPlayStr('Effort')
        actual = wp_str.is_abecedarian()
        expected = True
        self.assertEqual(expected, actual)

    def test_is_abecedarian_5(self):
        '''Test is_abecedarian with a non-abecedarian word.'''
        wp_str = prj.WordPlayStr('ones')
        actual = wp_str.is_abecedarian()
        expected = False
        self.assertEqual(expected, actual)

    def test_is_abecedarian_6(self):
        '''Test is_abecedarian reversed with a non-reversed abecedarian word.'''
        wp_str = prj.WordPlayStr('almost')
        actual = wp_str.is_abecedarian(desc=True)
        expected = False
        self.assertEqual(expected, actual)

    def test_abecedarian_7(self):
        '''Test is_abecedarian reversed with a reversed abecedarian word.'''
        wp_str = prj.WordPlayStr('one')
        actual = wp_str.is_abecedarian(desc=True)
        expected = True
        self.assertEqual(expected, actual)


class TestIsPalindrome(unittest.TestCase):
    '''unittest test methods for is_palindrome.'''

    def test_is_palindrome_1(self):
        '''Test is_palindrome with an empty string.'''
        wp_str = prj.WordPlayStr('')
        actual = wp_str.is_palindrome()
        expected = True
        self.assertEqual(expected, actual)

    def test_is_palindrome_2(self):
        '''Test is_palindrome with a single character.'''
        wp_str = prj.WordPlayStr('a')
        actual = wp_str.is_palindrome()
        expected = True
        self.assertEqual(expected, actual)

    def test_is_palindrome_3(self):
        '''Test is_palindrome with two characters, palindrome.'''
        wp_str = prj.WordPlayStr('aa')
        actual = wp_str.is_palindrome()
        expected = True
        self.assertEqual(expected, actual)

    def test_is_palindrome_4(self):
        '''Test is_palindrome with two characters, not palindrome.'''
        wp_str = prj.WordPlayStr('ab')
        actual = wp_str.is_palindrome()
        expected = False
        self.assertEqual(expected, actual)

    def test_is_palindrome_5(self):
        '''Test is_palindrome with three (=odd) characters, palindrome.'''
        wp_str = prj.WordPlayStr('aba')
        actual = wp_str.is_palindrome()
        expected = True
        self.assertEqual(expected, actual)

    def test_is_palindrome_6(self):
        '''Test is_palindrome with three (=odd) characters, not palindrome.'''
        wp_str = prj.WordPlayStr('abc')
        actual = wp_str.is_palindrome()
        expected = False
        self.assertEqual(expected, actual)

    def test_is_palindrome_7(self):
        '''Test is_palindrome with a longer even string, palindrome.'''
        wp_str = prj.WordPlayStr('redder')
        actual = wp_str.is_palindrome()
        expected = True
        self.assertEqual(expected, actual)

    def test_is_palindrome_8(self):
        '''Test is_palindrome with a longer even string, not palindrome.'''
        wp_str = prj.WordPlayStr('renter')
        actual = wp_str.is_palindrome()
        expected = False
        self.assertEqual(expected, actual)

    def test_is_palindrome_9(self):
        '''Test is_palindrome with a longer odd string, palindrome.'''
        wp_str = prj.WordPlayStr('racecar')
        actual = wp_str.is_palindrome()
        expected = True
        self.assertEqual(expected, actual)

    def test_is_palindrome_10(self):
        '''Test is_palindrome with a longer odd string, not palindrome.'''
        wp_str = prj.WordPlayStr('bananas')
        actual = wp_str.is_palindrome()
        expected = False
        self.assertEqual(expected, actual)

class TestDocTest(unittest.TestCase):
    '''unittest test methods for doctest.'''

    def test_doctest_testmod(self):
        '''Test doctests.'''
        test_results = doctest.testmod(prj)
        actual = test_results[0]
        expected = 0
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
