import unittest
import toronto2.a1 as a1


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_num_buses_1(self):
        '''Test num_buses with ....'''
        actual = a1.num_buses('')
        expected = True
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit=False)
