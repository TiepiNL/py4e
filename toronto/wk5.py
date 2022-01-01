from operator import add
from functools import reduce

q = 10

# Q2


def mystery(s):
    i = 0
    result = ''

    while not s[i].isdigit():
        result = result + s[i]
        i = i + 1

    return result


# Q3
def example(L):
    """ (list) -> list
    """
    i = 0
    result = []
    while i < len(L):
        result.append(L[i])
        i = i + 3
    return result

# Q4


def compress_list(L):
    """ (list of str) -> list of str

    Return a new list with adjacent pairs of string elements
    from Lconcatenated together, starting with indices 0 and 1,
    2 and 3,and so on.

    Precondition: len(L) >= 2 and len(L) % 2 == 0

    >>> compress_list(['a', 'b', 'c', 'd'])
    ['ab', 'cd']
    """
    compressed_list = []
    i = 0

    while i < len(L):
        compressed_list.append(L[i] + L[i + 1])
        # MISSING CODE HERE
        i = i + 2

    return compressed_list


# Q6
def while_version(L):
    """ (list of number) -> number
    """
    i = 0
    total = 0

    while i < len(L) and L[i] % 2 != 0:
        total = total + L[i]
        i = i + 1

    return total


def for_version1(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0:
            total = total + num
        found_even = True

    return total


def for_version2(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0:
            total = total + num
            found_even = True

    return total


def for_version3(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0:
            total = total + num
        elif not found_even:
            found_even = True

    return total


def for_version4(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0 and not found_even:
            total = total + num
        else:
            found_even = True

    return total


# Q9
def cap_song_repetition1(playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.

    '''
    while playlist.count(song) > 3:
        playlist.pop(song)


def cap_song_repetition2(playlist, song):
    while playlist.count(song) > 3:
        playlist.remove(playlist.index(song))


def cap_song_repetition3(playlist, song):
    while playlist.count(song) > 3:
        playlist.remove(song)


def cap_song_repetition4(playlist, song):
    while playlist.count(song) >= 3:
        playlist.remove(song)


def cap_song_repetition5(playlist, song):
    while playlist.count(song) > 3:
        playlist.pop(playlist.index(song))


# Q12
def increment_items(L, increment):
    i = 0
    while i < len(L):
        L[i] = L[i] + increment
        i = i + 1


if q == 1:
    # Select the expression(s) that evaluate to \color{black}{\verb|True|}True.
    print(int('3') in [len('a'), len('ab'), len('abc')])  # True
    print('a' in ['mom', 'dad'])                          # False
    print(len('mom') in [1, 2, 3])                        # True
    print('3' in [1, 2, 3])                               # False
    #print([1, 2, 3] in len('mom'))                        # TypeError
    print(len([1, 2, 3]) == len(['a', 'b', 'c']))         # True

elif q == 2:
    # Select the function call(s) that result in an error.
    print(mystery('abc123'))  # 'abc'
    print(mystery('123'))     # ''
    print(mystery('123abc'))  # ''
    #print(mystery('abc'))     # IndexError

elif q == 3:
    # Which is the best docstring description for function 'example'?
    print(example([1, 10, 50, 100, 20, 40, 30, 66, 33, 22]))
    # Return a list containing every third item from L starting at index 0.  # OK
    # Return an empty list.
    # Return a list containing every third index from L starting at index 0.
    # Return a list containing the items from L starting from index 0, omitting every third item.

elif q == 4:
    # Select the missing line of code.
    print(compress_list([1, 2, 3, 4, 5, 6]))
    # i = i + 1
    # i = i + i
    # i = i * 2
    # i = i + 2   # OK

elif q == 5:
    # What is the sum of the odd/even numbers from x through y, inclusive?
    # Hint: write a while loop to accumulate the sum and print it. Then copy
    # and paste that sum. For maximum learning, do it with a for loop as well,
    # using range.
    startnbr = 1523
    endnbr = 10503
    endnbr_incl = 10503 + 1

    # reduce:
    # Apply function of two arguments cumulatively to the items of iterable,
    # from left to right, so as to reduce the iterable to a single value.
    print(reduce(add, range(startnbr, endnbr_incl, 2)))
    # 27541388

elif q == 6:
    # The while loop stops as soon as an even number is found, and the sum of all
    # the previous numbers is returned.

    # The four functions below use a for loop to try to accomplish the same task,
    # although they keep iterating through all of the numbers in L regardless of
    # whether the numbers are even or odd.  Only one of them returns the same
    # value as function while_version.  Which one is it?
    print(while_version([1, 3, 7, 10, 1, 2, 6]))  # 11
    print(for_version1([1, 3, 7, 10, 1, 2, 6]))   # 12
    print(for_version2([1, 3, 7, 10, 1, 2, 6]))   # 12
    print(for_version3([1, 3, 7, 10, 1, 2, 6]))   # 12
    print(for_version4([1, 3, 7, 10, 1, 2, 6]))   # 11 OK

elif q == 7:
    # Which of the following code fragments(s) could be the missing code in
    # the program above?

    letters = ['b', 'd', 'a']
    # MISSING CODE HERE
    #letters = letters.sort()  # None
    letters.sort()            # ['a', 'b', 'd'] OK
    #letters = sort(letters)   # NameError
    #sort(letters)             # NameError

    print(letters)
    #['a', 'b', 'd']

elif q == 8:
    fruits = ['banana', 'apple', 'pear', 'peach']
    fruits.insert(fruits.index('pear'), 'watermelon')
    print(fruits)
    # What is printed by the code above?
    #['banana', 'apple', 'watermelon', 'pear', 'peach']   # OK
    #['banana', 'apple', 'pear', 'watermelon', 'peach']
    #['banana', 'watermelon', 'apple', 'pear', 'peach']
    #['banana', 'apple', 'watermelon', 'peach']
    veggies = ['carrot', 'broccoli', 'potato', 'asparagus']
    veggies.insert(veggies.index('broccoli'), 'celery')
    print(veggies)

elif q == 9:
    # Your younger sibling has just discovered music from the 1970's. They have put
    # together a playlist of the same 5 songs repeated again and again.
    # Here is an example of their playlist:
    # ['Lola', 'Venus', 'Lola', 'Lola', 'Let It Be', 'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola']
    # You want to make sure that Lola gets played at most 3 times,
    # so you want to complete this function that edits the playlist:
    songs1 = ['Lola', 'Venus', 'Lola', 'Lola', 'Let It Be',
              'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola']
    song = 'Lola'
    #cap_song_repetition1(songs1, song)                        # TypeError
    #print(songs1.count('Lola'))
    songs2 = ['Lola', 'Venus', 'Lola', 'Lola', 'Let It Be',
              'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola']
    #cap_song_repetition2(songs2, song)                        # ValueError
    #print(songs2.count('Lola'))
    songs3 = ['Lola', 'Venus', 'Lola', 'Lola', 'Let It Be',
              'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola']
    cap_song_repetition3(songs3, song)                        # 3   OK
    print(songs3.count('Lola'))
    songs4 = ['Lola', 'Venus', 'Lola', 'Lola', 'Let It Be',
              'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola']
    cap_song_repetition4(songs4, song)                        # 2
    print(songs4.count('Lola'))
    songs5 = ['Lola', 'Venus', 'Lola', 'Lola', 'Let It Be',
              'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola']
    cap_song_repetition5(songs5, song)                        # 3   OK
    print(songs5.count('Lola'))

elif q == 10:
    # Which of the following code fragments(s) could be the missing code in the program above?
    a = [1, 2, 3]
    b = a
    # MISSING CODE HERE
    b[1] = 'AB'          # [1, 'A', 3] [1, 'A', 3]   OK
    a[1] = a[1][0]

    b[-2] = 'A'          # [1, 'A', 3] [1, 'A', 3]   OK

    a[1] = 'A'           # [1, 'A', 3] [1, 'A', 3]   OK

    a = [1, 'A', 3]      # [1, 'A', 3] [1, 'A', 3]   OK
    b = [1, 'A', 3]

    print(a, b)
    #[1, 'A', 3][1, 'A', 3]

elif q == 11:
    # Which of the following code fragments(s) could be the missing code in the program above?
    a = [1, 2, 3]
    b = [1, 2, 3]
    # MISSING CODE HERE
    #b[1] = 'AB'          # TypeError
    #a[1] = a[1][0]

    #b[-2] = 'A'          # [1, 2, 3] [1, 'A', 3]

    #a[1] = 'A'           # [1, 'A', 3] [1, 2, 3]

    a = [1, 'A', 3]      # [1, 'A', 3] [1, 'A', 3]  OK
    b = [1, 'A', 3]

    print(a, b)
    #[1, 'A', 3][1, 'A', 3]

elif q == 12:
    values = [1, 2, 3]
    print(increment_items(values, 2))
    print(values)
    # What is printed by the program above?

    #None
    #[1, 2, 3]

    #None            # OK
    #[3, 4, 5]

    #[3, 4, 5]
    #None

    #[3, 4, 5]
    #[1, 2, 3]

elif q == 13:
    # Select the code fragment(s) that print [3, 6, 9].
    values = []                      # [3, 6, 9]   OK
    for num in range(3, 10, 3):
        values.append(num)
    print(values)

    values = []                      # [3, 6, 9]   OK
    for num in range(1, 4):
        values.append(num * 3)
    print(values)

    values = []                      # [3, 6]
    for num in range(3, 9, 3):
        values.append(num)
    print(values)

    values = []                      # [3, 6]
    for num in range(1, 3):
        values.append(num * 3)
    print(values)

elif q == 14:
    # Select the function calls to range that, when used to fill in the blank,
    # cause the code to produce the results below.
    #for num in __________________:
    #print(num)
    # The loop should print this:
    #3
    #11
    #19
    for num in range(3, 20, 8):     # 3, 11, 19   OK
        print(num)
    print('')

    for num in range(3, 23, 8):     # 3, 11, 19   OK
        print(num)
    print('')

    for num in range(3, 8, 20):     # 3
        print(num)
    print('')

    for num in range(3, 19, 8):     # 3, 11
        print(num)
