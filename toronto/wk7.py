# Q11
def eat(d):
    '''(dict of {str: int}) -> bool

    Each key in d is a fruit and each value is the quantity of     that fruit.

    REST OF DESCRIPTION MISSING HERE

    >>> eat({'apple': 2, 'banana': 3, 'pear': 3, 'peach': 1})
    True
    >>> eat({'apple': 0, 'banana': 0})
    False
    '''
    ate = False
    for fruit in d:
        if d[fruit] > 0:
            d[fruit] = d[fruit] - 1
            ate = True

    return ate

# Q12


def contains(v, d):
    ''' (object, dict of {object: list}) -> bool

    Return whether v is an element of one of the list values in    d.
    >>> contains('moogah', {1: [70, 'blue'], 2: [1.24, 'moogah'    , 90], 3.14: [80, 100]})
    True
    >>> contains('moogah', {'moogah': [1.24, 'frooble', 90], 3.    14: [80, 100]})
    False
    '''

    found = False  # Whether we have found v in a list in d.

    # CODE MISSING HERE
    #for k in d:                            # False/False
    #    for i in range(len(d[k])):
    #        found = (d[k][i] == v)

    #for k in d:                            # False/True
    #    if v == k:
    #        found = True

    #for k in d:                            # True/False
    #    if v in d[k]:
    #        found = True

    for k in d:                             # True/False
        for i in range(len(d[k])):
            if d[k][i] == v:
                found = True

    return found


q = 12

if q == 1:
    # Consider this code:
    d = {'a': 1, 'b': 2}
    # CODE MISSING HERE
    d['c'] = 3
    print(d)
    # {'a': 1, 'c': 3, 'b': 2}

    # Write the missing assignment statement that that modifies the dictionary as shown.
    # (Just write the assignment statement; don't write the >>> part.)
    # d['c'] = 3


elif q == 2:
    # Consider this code:
    d = {'a': 1, 'b': 2}
    # CODE MISSING HERE
    d['b'] = 3
    print(d)
    #{'a': 1, 'b': 3}

    # Write the missing assignment statement that modifies the dictionary as shown.
    # (Just write the assignment statement; don't write the >>> part.)
    # d['b'] = 3


elif q == 3:
    # Consider this code:
    d = {'a': [1, 3], 'b': [5, 7]}
    # CODE MISSING HERE
    d['a'].insert(1, 2)        # OK

    #d['a'].append(2)           # OK
    #d['a'].sort()

    #d['a'].insert(2, 1)        # {'a': [1, 3, 1], 'b': [5, 7]}

    #d['A'].insert(1, 2)        # KeyError:

    print(d)
    #{'a': [1, 2, 3], 'b': [5, 7]}

    # Select the option(s) that would lead to this result. Hint: call help on insert,
    # append, and sort.


elif q == 4:
    # Consider this assignment statement:
    d = {'a': 1, 'c': 3, 'b': 2}

    # Select the expression(s) that evaluate to True.
    print(not ('e' in d))   # True
    print(2 in d)           # False
    print("b" in d)         # True
    print('B' in d)         # False


elif q == 5:
    # Consider this code:
    d = {'a': [1, 3], 'b': [5, 7, 9], 'c': [11]}

    # Select the expression(s) that evaluate to 3.
    print(len(d['a']) + len(d['c']))   # 3  OK
    print(len(d['a']))                 # 2
    print(len(d['b']))                 # 3  OK
    #print(len(d['a' + 'c']))          # KeyError:


elif q == 6:
    # Consider this code:
    tup = (1, 2, 3)

    # Select the expression(s) and statement(s) below that result in an error.
    #tup[-2] = 4              # TypeError       OK
    print(tup.count(3))       # 1
    #print(tup.append(4))     # AttributeError  OK
    print(tup[0] == tup[-1])  # False


elif q == 7:
    # Select the expression(s) that can be used as dictionary keys.
    d = {}
    key1 = ['a', 'b']
    key2 = {1: 2, 3: 4}
    key3 = (1, 'fred', 2.0)
    key4 = ('single',)

    #d[key1] = 'value1'     # TypeError: unhashable type: 'list'
    #d[key2] = 'value2'     # TypeError: unhashable type: 'dict'
    d[key3] = 'value3'      # {(1, 'fred', 2.0): 'value3'}
    d[key4] = 'value4'      # {('single',): 'value4'}
    print(d)

elif q == 8:
    # Consider this code:
    #d = {1: ['a', 'b', 'c'], 2: ['d', 'e'], 3: []}

    # Select the code fragment(s) that set variable total to the number of items
    # in all the lists that occur as values in d.
    d = {1: ['a', 'b', 'c'], 2: ['d', 'e'], 3: []}
    L = []
    for k in d:
        L.extend(d[k])
    total = len(L)
    print(total)           # 5  OK

    d = {1: ['a', 'b', 'c'], 2: ['d', 'e'], 3: []}
    total = 0
    for k in d:
        total = total + len(d[k])
    print(total)           # 5  OK

    d = {1: ['a', 'b', 'c'], 2: ['d', 'e'], 3: []}
    L = []
    for k in d:
        L.append(k)
    total = len(L)
    print(total)           # 3 (key/val pairs in dict)

    d = {1: ['a', 'b', 'c'], 2: ['d', 'e'], 3: []}
    total = 0
    for k in d:
        total = total + k
    print(total)           # 6 (sum of loop index k 1+2+3)


elif q == 9:
    # This dictionary has 3 keys that are all the same. Enter this in the Python shell:
    {1: 10, 1: 20, 1: 30}

    # Submit what the code above evaluates to; don't submit your answers to the thought
    # questions below.
    {1: 30}

    # What we want you to think about: We haven't covered this situation in the videos;
    # what do you think should happen? Do you think this should cause an error?
    # Should it discard some of the key/value pairs? If so, which one do you think it should keep?
    # People who create programming languages have to make these kinds of decisions,
    # and often there isn't a clear good choice.


elif q == 10:
    # Consider this code:
    L = [['apple', 3], ['pear', 2], ['banana', 3]]
    d = {}
    for item in L:
        d[item[0]] = item[1]
    print(d)
    # What does this code do?
    # * Populates dictionary d where each key is the first item of each inner list of L     OK
    #   and each value is the second item of that inner list.
    # * Reorders the items in the inner lists of L.
    # * Populates dictionary L where each key is the first item of each inner list of d
    #   and each value is the second item of that inner list.
    # * Removes the items from L and populates dictionary d where each key is the first item
    #   of each inner list of L and each value is the second item of that inner list.


elif q == 11:
    d = {'banana': 3, 'apple': 5, 'orange': 1}
    eat(d)
    print(d)
    # Select the most appropriate description below.
    # * Reduce by 1 all quantities greater than 0 associated with each fruit in d.
    # * Remove from d all fruits that have a value of 0 associated with them and return
    #   True if and only if the were no such fruits.
    # * Return True if and only if any fruit was eaten.
    # * Try to eat one of each fruit: reduce by 1 all quantities greater than 0 associated
    #   with each fruit in d and return True if and only if any fruit was eaten.              OK


elif q == 12:
    # Select the code fragment(s) that make the function above match its docstring description.
    print(contains('moogah', {1: [70, 'blue'], 2: [
          1.24, 'moogah', 90], 3.14: [80, 100]}))  # True
    # False
    print(
        contains('moogah', {'moogah': [1.24, 'frooble', 90], 3.14: [80, 100]}))
