'''
Math functionsc for all kinds of calculations
'''

def sum_of_range(begin, end):
    ''' (int, int) -> int

    Returns the sum of a numeric range from 'begin' to 'end', inclusive.

    >>> sum_of_range(1, 23)
    276
    >>> sum_of_range(5, 104933942581744275610)
    5505566152874402176661682623817726296064
    '''
    to_begin = (begin-1) * ((begin-1) / 2 + 0.5)
    from_one = end * (end / 2 + 0.5)
    from_begin = from_one - to_begin
    return int(from_begin)

if __name__ == '__main__':
    import doctest
    doctest.testmod()


# https://en.wikipedia.org/wiki/Fibonacci_number