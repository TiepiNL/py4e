import pathlib
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
            lines = fopen.readlines()
    except OSError as err:
        logtxt = f"Can't open file: '{file}'. {err}."
        print(logtxt)
        sys.exit(1)

    return lines
