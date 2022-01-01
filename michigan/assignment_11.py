"""
Finding Numbers in a Haystack
In this assignment you will read through and parse a file with text and numbers.
You will extract all the numbers in the file and compute the sum of the numbers.

Handling The Data
The basic outline of this problem is to read the file, look for integers using
the re.findall(), looking for a regular expression of '[0-9]+' and then converting
the extracted strings to integers and summing up the integers.
"""

import pathlib
import re
import sys

def read_textfile(file):
    """
    Open a text file and return the content.
    :param file: the file to read.
    :return: all lines in the file (list)
    """
    file_path = pathlib.Path(file)
    try:
        with file_path.open(mode="r", encoding="utf-8") as fopen:
            file_content = fopen.readlines()
    except OSError as err:
        logtxt = f"Can't open file: '{file}'. {err}."
        print(logtxt)
        sys.exit(1)
    return file_content


def get_numbers(content_string):
    """
    Retrieve all the numbers in a string.
    :param content_string: the string to check.
    :return: list with numbers.
    """
    numlist = list()
    for line in content_string:
        line = line.rstrip()
        numbers = re.findall("[0-9]+", line)
        for num in numbers:
            numlist.append(int(num))
    return numlist

name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_42.txt"
lines = read_textfile(name)

# Method 1 - double for-loop
nbrs = get_numbers(lines)
print(sum(nbrs))

# Method 2 - Optional: Just for Fun
print(sum([int(i) for i in re.findall('[0-9]+', str(lines))]))
