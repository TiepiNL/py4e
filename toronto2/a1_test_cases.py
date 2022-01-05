'''
CHOOSE TEST CASES
write down a table containing:
* a description of each test,
* the values of the arguments, and
* the expected result.

REQUIREMENTS
python -m pip install -U prettytable
'''

import json
import pathlib
import sys
from prettytable import PrettyTable


def read_textfile(file):
    """
    Open a text file and return the content.
    """
    file_path = pathlib.Path(file)
    try:
        with file_path.open(mode="r", encoding="utf-8") as fopen:
            lines = fopen.read()        # string
            #lines = fopen.readlines()   # list
    except OSError as err:
        logtxt = f"Can't open file: '{file}'. {err}."
        print(logtxt)
        sys.exit(1)

    return lines


jsn = json.loads(read_textfile('a1_test_cases.json'))
header = ['#', 'Argument values', 'Expected result', 'Description']
for func in ['num_buses', 'stock_price_summary', 'swap_k']:
    t = PrettyTable(header)
    rownr = 1
    for case in jsn[func]:
        t.add_row([rownr, case['arguments'], case['expected'], case['description']])
        rownr += 1
    print(func.upper())
    print(t,'\n\n')
