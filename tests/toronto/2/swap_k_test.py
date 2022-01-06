import unittest
import toronto2.a1 as a1


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_swap_k_1(self):
        '''Test swap_k with an empty list with zero swaps.'''
        actual = []
        a1.swap_k(actual, 0)
        expected = []
        self.assertEqual(expected, actual)

    def test_swap_k_2(self):
        '''Test swap_k with zero swaps (stays untouched).'''
        actual = [1, 2, 3]
        a1.swap_k(actual, 0)
        expected = [1, 2, 3]
        self.assertEqual(expected, actual)

    def test_swap_k_3(self):
        '''Test swap_k with an int-based multi-char swap in a list with an even number of items.'''
        actual = [1, 2, 3, 4, 5, 6]
        a1.swap_k(actual, 2)
        expected = [5, 6, 3, 4, 1, 2]
        self.assertEqual(expected, actual)

    def test_swap_k_4(self):
        '''Test swap_k with a list with an odd number of items.'''
        actual = [1, 2, 3, 4, 5, 6, 7]
        a1.swap_k(actual, 3)
        expected = [5, 6, 7, 4, 1, 2, 3]
        self.assertEqual(expected, actual)

    def test_swap_k_5(self):
        '''Test swap_k with a string-based list with a minimum number of elements (2).'''
        actual = ['abc', 'xyz']
        a1.swap_k(actual, 1)
        expected = ['xyz', 'abc']
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
