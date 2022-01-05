# Q3
def f(x):
    y = x * 3
    return y - x


# Q5
def count_max_letters(s1, s2, letter):
    '''(str, str, str) -> int 

    s1 and s2 are strings, and letter is a string of length 1.
    Count how manytimes letter appears in s1 and in s2, and return the bigger of the two counts.

    >>> count_max_letters('hello', 'world', 'l')
    2
    >>> count_max_letters('cat', 'abracadabra', 'a')
    5
    '''

    # CODE MISSING HERE
    return max(s1.count(letter), s2.count(letter))


# Q6
def both_start_with(s1, s2, prefix):
    '''(str, str, str) -> bool

    Return True if and only if s1 and s2 both start with the letters in prefix.
    '''
    #if s1.startswith(prefix) and s2.startswith(prefix):
    #    return True
    #else:
    #    return False
    return s1.startswith(prefix) and s2.startswith(prefix)


# Q8
def gather_every_nth(L, n):
    '''(list, int) -> list

    Return a new list containing every n'th element in L, starting at index 0.

    Precondition: n >= 1

    >>> gather_every_nth([0, 1, 2, 3, 4, 5], 3)

    [0, 3]
    >>> gather_every_nth(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], 2)
    ['a', 'c', 'e', 'g', 'i']
    '''

    result = []
    i = 0
    while i < len(L):
        result.append(L[i])
        i = i + n  # CODE MISSING HERE

    return result


# Q9
def get_keys(L, d):
    '''(list, dict) -> list

    Return a new list containing all the items in L that are keys in d.

    >>> get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'})
    [1, 'a']
    '''

    result = []
    for k in L:  # CODE MISSING HERE
        if k in d:
            result.append(k)

    return result


# Q10
def are_lengths_of_strs(L1, L2):
    '''(list of int, list of str) -> bool

    Return True if and only if all the ints in L1 are the lengths of the strings
    in L2 at the corresponding positions.

    Precondition: len(L1) == len(L2)

    >>> are_lengths_of_strs([4, 0, 2], ['abcd', '', 'ef'])
    True
    '''

    result = True
    for i in range(len(L1)):
        if L1[i] != len(L2[i]):  # CODE MISSING HERE
            result = False

    return result


# Q11
def double_last_value(L):
    '''(list of int) -> NoneType

    Double the value at L[-1]. For example, if L[-1] is 3,
    replace it with 6.

    Precondition: len(L) >= 1.
    '''
    L[-1] = L[-1] * 2


# Q12
def get_diagonal_and_non_diagonal(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the values on the
    diagonal of square nested list L and the second item is a list of the rest
    of the values in L.

    >>> get_diagonal_and_non_diagonal([[1,  3,  5], [2,  4,  5], [4,  0,  8]])
    ([1, 4, 8], [3, 5, 2, 5, 4, 0])

    r0c0 r0c1 r0c2
    r1c0 r1c1 r1c2
    r2c0 r2c1 r2c2
    '''

    diagonal = []
    non_diagonal = []
    for row in range(len(L)):
        for col in range(len(L)):

            # CODE MISSING HERE
            #if row == col:                          # OK
            #    diagonal.append(L[row][col])
            #elif row != col:
            #    non_diagonal.append(L[row][col])

            #if row == col:                          # OK
            #    diagonal.append(L[row][row])
            #else:
            #    non_diagonal.append(L[row][col])

            #if row == col:                          # ([1, 4, 8], [1, 3, 5, 2, 4, 5, 4, 0, 8])
            #    diagonal.append(L[row][col])
            #non_diagonal.append(L[row][col])

            #if row == col:                          # OK
            #    diagonal.append(L[row][col])
            #else:
            #    non_diagonal.append(L[row][col])

            if row == col:                          # OK
                diagonal.append(L[row][col])
            if row != col:
                non_diagonal.append(L[row][col])

    return (diagonal, non_diagonal)


# Q13
def add_to_letter_counts(d, s):
    '''(dict of {str: int}, str) -> NoneType

    d is a dictionary where the keys are single-letter strings and the values
    are counts.

    For each letter in s, add to that letter's count in d.

    Precondition: all the letters in s are keys in d.

    >>> letter_counts = {'i': 0, 'r': 5, 'e': 1}
    >>> add_to_letter_counts(letter_counts, 'eerie')
    >>> letter_counts
    {'i': 1, 'r': 6, 'e': 4}
    '''

    for c in s:
        # CODE MISSING HERE
        # increase the value (int) of the key c(har) with one
        d[c] = d[c] + 1


q = 13

if q == 1:
    # Select the expression(s) that evaluate to a float value.
    print(7 + 8.5)    # True
    print(8.0 % 4)    # True
    print(8 % 6)      # False
    print(3 // 4)     # False

elif q == 2:
    # Consider this code:
    a = 7
    b = a + 3
    a = 9
    # After the code above has been executed, what value does b refer to?
    print(b)
    # 10


elif q == 3:
    # What value is returned by a call on function f with argument 10?
    print(f(10))
    # 20


elif q == 4:
    # Consider this code:
    start = 'L'
    middle = 8
    end = 'R'
    # Write an expression that evaluates to the string 'L8R' using only the variables
    # start, middle, end, one call on function str, and string concatenation.
    # Do not use unnecessary parentheses: you need them for the function call, but nothing else.
    print(start + str(middle) + end)

elif q == 5:
    # The expression for the return statement is missing.  Write that expression below.
    # Use only the parameters, one call on function max, and two calls on str method count.

    # Do not use unnecessary parentheses: you need them for the function and method calls,
    # but nothing else. Do not include the word return, just write the expression.

    # max(s1.count(letter), s2.count(letter))
    print(count_max_letters('abracadrabra', 'lalaland', 'a'))
    print(count_max_letters('hello', 'world', 'l'))
    print(count_max_letters('cat', 'abracadabra', 'a'))

elif q == 6:
    # The function works, but the if statement can be replaced with a single return statement.
    # Write the missing expression. Use only the parameters, two calls on method startswith,
    # and operator and.
    # Do not use unnecessary parentheses: you need them for the method calls, but nothing else.
    # Do not include the word return, just write the expression.

    # s1.startswith(prefix) and s2.startswith(prefix)
    print(both_start_with('Mikael', 'Milou', 'Mi'))

elif q == 7:
    # Consider these two functions; we provide only the headers, type contracts, and a precondition:

    #def moogah(a, b):
    #'''(str, int) -> str'''

    #def frooble(L):
    #'''(list of str) -> int
    #Precondition: L has at least one element.'''

    # Below are code fragments that call these two functions in various ways. Select the
    # code fragment(s) below that are valid according to the function headers and the type contracts.

    # * moogah('a', moogah(['a']))
    # * moogah(frooble(['a']), 'a')
    # * lst = ['a', 'b', 'c']
    #   moogah(lst[0], len(lst))      # OK
    # * moogah('a', frooble(['a']))   # OK
    pass

elif q == 8:
    # Write the missing expression. Do not use parentheses. Do not include "i =".
    # Just write the missing expression.
    #i + n

    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    new_lst = gather_every_nth(lst, 3)
    print(new_lst)

elif q == 9:
    # Write the missing code for the first line of the for loop — everything after
    # the word "for", up to and including the colon :.
    # Do not use any parentheses, and do not call any functions or methods.
    # k in L:

    print(get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'}))
    #[1, 'a']


elif q == 10:
    # Write the missing code for the if statement — everything after the word "if",
    # up to and including the colon :.
    # Your answer should be of the form expr1 != expr2: , where expr1 and expr2 are expressions.
    # Use only variables i, L1, L2, indexing, and function len.
    # Do not use parentheses except for the call on len.
    # L1[i] != len(L2[i]):

    print(are_lengths_of_strs([4, 0, 2], ['abcd', '', 'ef']))
    #True

elif q == 11:
    # Consider this code:
    L1 = [1, 3, 5]
    double_last_value(L1)
    print(L1[-1])
    # Enter the number that gets printed.
    #10

elif q == 12:
    # Select the code fragment(s) that correctly complete this function.

    #if row == col:                          # OK
    #    diagonal.append(L[row][col])
    #elif row != col:
    #    non_diagonal.append(L[row][col])

    #if row == col:                          #
    #    diagonal.append(L[row][row])
    #else:
    #    non_diagonal.append(L[row][col])

    #if row == col:                          #
    #    diagonal.append(L[row][col])
    #non_diagonal.append(L[row][col])

    #if row == col:                          #
    #    diagonal.append(L[row][col])
    #else:
    #    non_diagonal.append(L[row][col])

    #if row == col:                          #
    #    diagonal.append(L[row][col])
    #if row != col:
    #    non_diagonal.append(L[row][col])

    print(get_diagonal_and_non_diagonal(
        [[1,  3,  5], [2,  4,  5], [4,  0,  8]]))
    #([1, 4, 8], [3, 5, 2, 5, 4, 0])

elif q == 13:
    # Write the missing assignment statement. Do not call any functions or methods.
    # Do not use unnecessary parentheses.
    #d[c] = d[c] + 1

    letter_counts = {'i': 0, 'r': 5, 'e': 1}
    add_to_letter_counts(letter_counts, 'eerie')
    print(letter_counts)
    #{'i': 1, 'r': 6, 'e': 4}
