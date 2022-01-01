"""
For Loops Over Indices, Parallel Lists and Strings, and Files
"""

q = 2

# Q1


def merge(L):
    merged = []
    for i in range(0, len(L), 3):
        merged.append(L[i] + L[i + 1] + L[i + 2])
    return merged


# Q2, Q3
def mystery(s):
    """ (str) -> bool
    """
    matches = 0
    for i in range(len(s) // 2):
        print(i)
        if s[i] == s[len(s) - 1 - i]:  # <--- How many times is this line reached?
            matches = matches + 1

    return matches == (len(s) // 2)


# Q4
def shift_right(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the rightand shift the    last item to the first position.

    Precondition: len(L) >= 1
    '''

    last_item = L[-1]

    # MISSING CODE GOES HERE
    #for i in range(len(L) - 1):
    #    L[i] = L[i + 1]

    #for i in range(1, len(L)):
    #    L[i] = L[i + 1]

    for i in range(1, len(L)):
        L[len(L) - i] = L[len(L) - i - 1]

    #for i in range(len(L)):
    #    L[i + 1] = L[i]

    L[0] = last_item


# Q5
def make_pairs(list1, list2):
    ''' (list of str, list of int) -> list of [str, int] list

    Return a new list in which each item is a 2-item list with
    the string from thecorresponding position of list1 and the
    int from the corresponding position of list2.

    Precondition: len(list1) == len(list2)

    >>> make_pairs(['A', 'B', 'C'], [1, 2, 3])
    [['A', 1], ['B', 2], ['C', 3]]
    '''

    pairs = []

    # CODE MISSING HERE
    #for i in range(len(list1)):     # [['C', 3]]
    #    inner_list = []
    #    inner_list.append(list1[i])
    #    inner_list.append(list2[i])
    #pairs.append(inner_list)

    for i in range(len(list1)):    # [['A', 1], ['B', 2], ['C', 3]]      OK
        pairs.append([list1[i], list2[i]])

    #for i in range(len(list1)):    # [['A', 1], ['B', 2], ['C', 3]]      OK
    #    inner_list = []
    #    inner_list.append(list1[i])
    #    inner_list.append(list2[i])
    #    pairs.append(inner_list)

    #inner_list = []                 [['A', 1, 'B', 2, 'C', 3], ['A', 1, 'B', 2, 'C', 3], ['A', 1, 'B', 2, 'C', 3]]
    #for i in range(len(list1)):
    #    inner_list.append(list1[i])
    #    inner_list.append(list2[i])
    #    pairs.append(inner_list)

    return pairs


# Q9
def contains(value, lst):
    """ (object, list of list) -> bool

    Return whether value is an element of one of the nested lists in lst.

    >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'], [80, 100]])
    True
    """

    found = False  # We have not yet found value in the list.

    # CODE MISSING HERE
    #for item in lst:                       # False
    #    if value == item:
    #        value = True

    #for i in range(len(lst)):              # False (doesn't stop after match)
    #    for j in range(len(lst[i])):
    #        found = (lst[i][j] == value)

    #for i in range(len(lst)):              # True     OK
    #    for j in range(len(lst[i])):
    #        if lst[i][j] == value:
    #            found = True

    for sublist in lst:                    # True     OK
        if value in sublist:
            found = True

    return found


# Q12
def lines_startswith(file, letter):
    """ (file open for reading, str) -> list of str

    Return the list of lines from file that begin with letter.
    The lines should have the newline removed.

    Precondition: len(letter) == 1
    """

    matches = []

    # CODE MISSING HERE
    for line in file:                            # OK
        if line.startswith(letter):
            matches.append(line.rstrip('\n'))

    #for line in file:                            # OK (IndexError last line if ''?)
    #    if letter == line[0]:
    #        matches.append(line.rstrip('\n'))

    #for line in file:
    #    if letter in line:
    #        matches.append(line.rstrip('\n'))

    #matches.append(line.startswith(letter).rstrip('\n'))

    return matches


# Q13
def write_to_file(file, sentences):
    """ (file open for writing, list of str) -> NoneType

    Write each sentence from sentences to file, one per line.

    Precondition: the sentences contain no newlines.
    """

    # CODE MISSING HERE
    i = 0
    for s in sentences:
        #file.write(s + '\n')        # OK
        file[i] = s + '\n'
        i += 1

    #file.write(sentences)

    #for s in sentences:             # No newlines
    #    file.write(s)

    #for s in sentences:             # OK
    #    file.write(s)
    #    file.write('\n')

    #for s in sentences:
    #    file.write(s)
    #file.write('\n')


if q == 1:
    print(merge([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    # What is printed by the code above?
    # [6, 15, 24]      # OK
    # [1, 4, 7]
    # [12, 15, 18]
    # [123, 456, 789]

elif q == 2:
    print(mystery('civil'))
    # Trace the function call mystery(’civil’) using the Python Visualizer.
    # How many times is the line marked above reached?
    # 2     OK

elif q == 3:
    # Which is the best docstring description for function mystery?
    # Return True if and only if s is equal to the reverse of s.                  OK
    # Return True if and only if s[:len(s) // 2]  is the same as s[len(s) // 2:].
    # Return True if and only if the number of duplicate characters in s is equal to len(s) // 2.
    # Return True if and only if there are exactly len(s) // 2 characters in s that are the same character.
    print(mystery('cbabc'))

elif q == 4:
    # In one of the Week 6 lecture videos, we wrote the function shift_left. Consider this function,
    # which shifts in the other direction.
    # Select the code fragment that correctly completes function shift_right.
    lst = [1, 2, 3, 4, 5]
    shift_right(lst)
    print(lst)

elif q == 5:
    # Select the code fragment(s) that make the function above match its docstring description.
    print(make_pairs(["A", "B", "C"], [1, 2, 3]))

elif q == 6:
    numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # Using numbers and indexing with non-negative indices, write an expression that evaluates to 7.
    # Do not use addition, subtraction, or parentheses ( ) (brackets ([] are required).
    print(numbers[2][0])

elif q == 7:
    breakfast = [['French', 'toast'], [
        'blueberry', 'pancakes'], ['scrambled', 'eggs']]
    # Using breakfast and indexing with only negative indices, write an expression that evaluates to
    # ’blueberry’. Do not use addition, subtraction, or parentheses ( ) (brackets [ ] are required).
    print(breakfast[-2][-2])

elif q == 8:
    c = 0
    for i in range(2, 5):
        for j in range(4, 9):
            c += 1
            #print(i, j)
    print(c)

    # How many times is print(i, j) executed?
    # 5
    # 24
    # 15
    # 3

elif q == 9:
    print(contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'], [80, 100]]))

elif q == 10:
    # A file has a section at the top that has a preamble describing the contents of the file,
    # then a blank line, then a list of high temperatures for each day in January all on one line,
    # then a list of high temperatures for each day in February all on one line, then lists for
    # March, April, and so on through December, each on one line.  There are thousands of lines of
    # information after that temperature data that you aren't currently interested in.

    # You want to write a program that prints the average of the high temperatures in January.
    # Which of the four file-reading approaches should you use?

    # The read approach
    print("The readline approach")      # OK
    # The readlines approach
    # The for line in file approach

elif q == 11:
    # data_file refers to a file open for reading.
    #for line in data_file:
    #    print(line)
    line = "fdf kljljl sdsa\n"
    # The program above prints the lines of the file but adds an extra blank line after each line.
    # Select the code fragment(s) that when used as replacement(s) for print(line) will print the
    # lines without extra blank lines.
    # Note: use help to find out information about any functions or methods that you are not familiar with.

    print(line, end='')           # OK
    #print(line - '\n')           # TypeError
    print(line.rstrip('\n'))      # OK
    #print(line.strip())          # Also removes regular blank lines!

elif q == 12:
    content = ["The old bag.\n", "Is not from me.\n", "It belongs to you.\n",
               "True that!\n", "Another line with words...\n", "Bye, say I!\n"]
    print(lines_startswith(content, "I"))

elif q == 13:
    lst = ["1", "2", "3", "4", "5", "6"]
    content = ["The old bag.", "Is not from me.", "It belongs to you.",
               "True that!", "Another line with words...", "Bye, say I!"]
    write_to_file(lst, content)
    print(lst)
