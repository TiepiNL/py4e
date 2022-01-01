import unittest             # The test framework
import path.module as prj   # The code to test


class ProjectTests(unittest.TestCase):
    def test_func1(self):
        testcases = []
        expected = []
        actuals = []
        for case in testcases:
            actuals.append(prj.func1(case))
        self.assertEqual(actuals, expected)

    def test_func2(self):
        testcases = [[],
                     [],
                     []
                     ]
        expected = ['', '', '']
        actuals = []
        for case in testcases:
            actuals.append(prj.func2(case[0], case[1]))
        self.assertEqual(actuals, expected)
