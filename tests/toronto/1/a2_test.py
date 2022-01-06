import unittest             # The test framework
import toronto1.a2 as prj    # The code to test


class A2Tests(unittest.TestCase):

    def test_is_valid_nucleotide(self):
        testcases = ['A', 'a', 'X', 'ACGTACG', '', '1', 1]
        expected = [True, False, False, False, False, False, False]
        actuals = []
        for case in testcases:
            actuals.append(prj.is_valid_nucleotide(case))
        self.assertEqual(actuals, expected)

    def test_is_valid_sequence(self):
        testcases = ['ACGTACG', 'ACGTXYZ', 'A', '', '1', 1]
        expected = [True, False, True, True, False, False]
        actuals = []
        for case in testcases:
            actuals.append(prj.is_valid_sequence(case))
        self.assertEqual(actuals, expected)

