'''
Symbol	I	V	X	L	C	D	M
Value	1	5	10	50	100	500	1000
'''
def decimal_to_roman(number):
    ''' (int) -> str

    Precondition: 3999 => number > 0

    >>> decimal_to_roman(1)
    'I'
    >>> decimal_to_roman(1115)
    'MCXV'
    >>> decimal_to_roman(484)
    'CDLXXXIV'
    >>> decimal_to_roman(2000)
    'MM'
    >>> decimal_to_roman(3999)
    'MMMCMXCIX'

    decimal_to_roman(0)
    ValueError: Number should be between 1 and 3999, inclusive.
    decimal_to_roman(4000)
    ValueError: Number should be between 1 and 3999, inclusive.
    '''
    if number > 3999 or number <= 0:
        raise ValueError("Number should be between 1 and 3999, inclusive.")

    sval = str(number)
    decimal_list = list(sval)
    decimal_list.reverse()
    digits = len(decimal_list)

    result = ''
    if digits == 4:
        thousands = {
            1: 'M',
            2: 'MM',
            3: 'MMM'
        }
        result += thousands[int(decimal_list[3])]

    if digits >= 3 and int(decimal_list[2]) != 0:
        hundreds = {
            1: 'C',
            2: 'CC',
            3: 'CCC',
            4: 'CD',
            5: 'D',
            6: 'DC',
            7: 'DCC',
            8: 'DCCC',
            9: 'CM'
        }
        result += hundreds[int(decimal_list[2])]

    if digits >= 2 and int(decimal_list[1]) != 0:
        tens = {
            1: 'X',
            2: 'XX',
            3: 'XXX',
            4: 'XL',
            5: 'L',
            6: 'LX',
            7: 'LXX',
            8: 'LXXX',
            9: 'XC'
        }
        result += tens[int(decimal_list[1])]

    if digits >= 1 and int(decimal_list[0]) != 0:
        units = {
            1: 'I',
            2: 'II',
            3: 'III',
            4: 'IV',
            5: 'V',
            6: 'VI',
            7: 'VII',
            8: 'VIII',
            9: 'IX'
        }
        result += units[int(decimal_list[0])]

    return result


def roman_to_decimal(numeral):
    ''' (str) -> int

    convert Roman numerals to a decimal number and return it.

    Precondition: 'roman' is a valid roman numeral.

    >>> roman_to_decimal('CDLXXXIV')
    484
    '''
    value = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    # Initialization
    previous = 0
    result = 0

    # Split the Roman numeral string into Roman symbols and
    # traverse through all characters, in reverse order.
    numeral_list = list(numeral)
    numeral_list.reverse()
    for i in range(len(numeral_list)):
        # Convert each symbol of Roman Numerals into the value it represents.
        symbol_value = value[numeral_list[i]]
        # If current value of symbol is greater than or equal to the value of next symbol,
        # then add this value to the running total. Otherwise subtract this value by adding
        # the value of next symbol to the running total.
        if symbol_value >= previous:
            result += symbol_value
        else:
            result -= symbol_value

        previous = symbol_value

    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
