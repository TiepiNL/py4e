'''
ASSIGNMENT
* Read and implement the three functions.
* Add additional examples to the docstring.
'''

import math

def num_buses(n):
    ''' (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(0)
    0
    >>> num_buses(1)
    1
    >>> num_buses(50)
    1
    >>> num_buses(51)
    2
    >>> num_buses(500)
    10
    >>> num_buses(501)
    11
    '''
    return math.ceil(n / 50)


def stock_price_summary(price_changes):
    ''' (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    >>> stock_price_summary([])
    (0, 0)
    >>> stock_price_summary([0])
    (0, 0)
    >>> stock_price_summary([0.01, 100])
    (100.01, 0)
    >>> stock_price_summary([-0.01, -100])
    (0, -100.01)
    '''
    gains = 0
    losses = 0
    for chg in price_changes:
        if chg > 0:
            gains += chg
        elif chg < 0:
            losses += chg
    return (gains, losses)


def swap_k(lst, k):
    ''' (list, int) -> NoneType

    Precondtion: 0 <= k <= len(lst) // 2

    Swap the first k items of lst with the last k items of lst.

    >>> nums = []
    >>> swap_k(nums, 0)
    >>> nums
    []
    >>> nums = [1, 2, 3]
    >>> swap_k(nums, 0)
    >>> nums
    [1, 2, 3]
    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    >>> nums = [1, 2, 3, 4, 5, 6, 7]
    >>> swap_k(nums, 3)
    >>> nums
    [5, 6, 7, 4, 1, 2, 3]
    >>> nums = ['abc', 'xyz']
    >>> swap_k(nums, 1)
    >>> nums
    ['xyz', 'abc']
    '''
    # Split lst in 3 parts and combine them in the swapped order.
    first_k = lst[:k]
    last_k = lst[len(lst)-k:]
    remaining = lst[k:len(lst)-k]
    swapped = last_k + remaining + first_k
    # Empty the list and extend it with the contnet of the new swapped list.
    lst.clear()
    lst.extend(swapped)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
