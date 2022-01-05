import doctest
import unittest
import toronto2.a1 as a1


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    def test_num_buses_1(self):
        '''Test num_buses with ....'''
        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_num_buses_2(self):
        '''Test num_buses with ....'''
        actual = a1.num_buses(1)
        expected = 1
        self.assertEqual(expected, actual)

    def test_num_buses_3(self):
        '''Test num_buses with ....'''
        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(expected, actual)

    def test_num_buses_4(self):
        '''Test num_buses with ....'''
        actual = a1.num_buses(51)
        expected = 2
        self.assertEqual(expected, actual)

    def test_num_buses_5(self):
        '''Test num_buses with ....'''
        actual = a1.num_buses(500)
        expected = 10
        self.assertEqual(expected, actual)

    def test_num_buses_6(self):
        '''Test num_buses with ....'''
        actual = a1.num_buses(501)
        expected = 11
        self.assertEqual(expected, actual)


class TestDocTest(unittest.TestCase):
    '''unittest test methods for doctest.'''

    def test_doctest_testmod(self):
        '''Test doctests.'''
        test_results = doctest.testmod(a1.num_buses)
        actual = test_results[0]
        expected = 0
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit=False)
