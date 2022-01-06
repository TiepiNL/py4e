import unittest
import toronto2.a1 as a1


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_stock_price_summary_1(self):
        '''Test stock_price_summary with an empty list.'''
        actual = a1.stock_price_summary([])
        expected = (0, 0)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_2(self):
        '''Test stock_price_summary with a single zero value.'''
        actual = a1.stock_price_summary([0])
        expected = (0, 0)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_3(self):
        '''Test stock_price_summary with a single positive value.'''
        actual = a1.stock_price_summary([0.01])
        expected = (0.01, 0)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_4(self):
        '''Test stock_price_summary with multiple positive values.'''
        actual = a1.stock_price_summary([0.01, 100])
        expected = (100.01, 0)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_5(self):
        '''Test stock_price_summary with multiple negative values.'''
        actual = a1.stock_price_summary([-0.01, -100])
        expected = (0, -100.01)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_6(self):
        '''Test stock_price_summary with multiple mixed values.'''
        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
