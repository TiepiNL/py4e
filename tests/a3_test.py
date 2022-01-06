import unittest             # The test framework
import toronto1.a3 as prj    # The code to test
import pathlib


class A3Tests(unittest.TestCase):

    def test_is_valid_word(self):
        testcases = [[['ANT', 'BOX', 'SOB', 'TO'], 'TO'],
                     [['ANT', 'BOX', 'SOB', 'TO'], 'OT']
                     ]
        expected = [True, False]
        actuals = []
        for case in testcases:
            actuals.append(prj.is_valid_word(case[0], case[1]))
        self.assertEqual(actuals, expected)

    def test_make_str_from_row(self):
        testcases = [[[['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0],
                     [[['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1],
                     [[['A', 'N', 'T', 'T', 'X', 'S', 'O', 'B']], 0]
                     ]
        expected = ['ANTT', 'XSOB', 'ANTTXSOB']
        actuals = []
        for case in testcases:
            actuals.append(prj.make_str_from_row(case[0], case[1]))
        self.assertEqual(actuals, expected)

    def test_make_str_from_column(self):
        testcases = [[[['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1],
                     [[['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B'], ['B', 'G', 'E', 'I']], 2],
                     ]
        expected = ['NS', 'TOE']
        actuals = []
        for case in testcases:
            actuals.append(prj.make_str_from_column(case[0], case[1]))
        self.assertEqual(actuals, expected)

    def test_board_contains_word_in_row(self):
        testcases = [[[['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB'],
                     [[['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'XOB']
                     ]
        expected = [True, False]
        actuals = []
        for case in testcases:
            actuals.append(prj.board_contains_word_in_row(case[0], case[1]))
        self.assertEqual(actuals, expected)

    def test_board_contains_word_in_column(self):
        testcases = [[[['A', 'T', 'N', 'T'], ['X', 'S', 'O', 'B']], 'NO'],
                     [[['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO']
                     ]
        expected = [True, False]
        actuals = []
        for case in testcases:
            actuals.append(prj.board_contains_word_in_column(case[0], case[1]))
        self.assertEqual(actuals, expected)

    def test_board_contains_word(self):
        testcases = [[[['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT'],
                     [[['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'PAN'],
                     [[['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO'],
                     [[['A', 'T', 'N', 'T'], ['X', 'S', 'O', 'B']], 'NO']
                     ]
        expected = [True, False, False, True]
        actuals = []
        for case in testcases:
            actuals.append(prj.board_contains_word(case[0], case[1]))
        self.assertEqual(actuals, expected)

    def test_word_score(self):
        testcases = ['AN', 'PAN', 'SIXSIX', 'FORTEEN', 'EIGHTTEEN', 'THIRTYPNTS']
        expected = [0, 3, 6, 14, 18, 30]
        actuals = []
        for case in testcases:
            actuals.append(prj.word_score(case))
        self.assertEqual(actuals, expected)

    def test_num_words_on_board(self):
        testcases = [[[['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO']]]
        expected = [3]
        actuals = []
        for case in testcases:
            actuals.append(prj.num_words_on_board(case[0], case[1]))
        self.assertEqual(actuals, expected)

    def test_read_words(self):
        testcases = ['.\\toronto\\wordslist1.txt']
        expected = [['CRUNCHY', 'COWS', 'EAT', 'GRASS']]
        actuals = []
        for case in testcases:
            file_path = pathlib.Path(case)
            try:
                with file_path.open(mode="r", encoding="utf-8") as fopen:
                    actuals.append(prj.read_words(fopen))
            except OSError:
                continue
        self.assertEqual(actuals, expected)

    def test_read_board(self):
        testcases = ['.\\toronto\\board1.txt']
        expected = [[['E', 'F', 'J', 'A', 'J', 'C', 'O', 'W', 'S', 'S'],
                     ['S', 'D', 'G', 'K', 'S', 'R', 'F', 'D', 'F', 'F'],
                     ['A', 'S', 'R', 'J', 'D', 'U', 'S', 'K', 'L', 'K'],
                     ['H', 'E', 'A', 'N', 'D', 'N', 'D', 'J', 'W', 'A'],
                     ['A', 'N', 'S', 'D', 'N', 'C', 'N', 'E', 'O', 'P'],
                     ['P', 'M', 'S', 'N', 'F', 'H', 'H', 'E', 'J', 'E'],
                     ['J', 'E', 'P', 'Q', 'L', 'Y', 'N', 'X', 'D', 'L']]
                     ]
        actuals = []
        for case in testcases:
            file_path = pathlib.Path(case)
            try:
                with file_path.open(mode="r", encoding="utf-8") as fopen:
                    actuals.append(prj.read_board(fopen))
            except OSError:
                continue
        self.assertEqual(actuals, expected)

if __name__ == '__main__':
    unittest.main()
