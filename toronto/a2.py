"""
A2 Problem Domain: Deoxyribonucleic Acid (DNA)

The problem domain for A2 is Deoxyribonucleic Acid (DNA), the double-stranded molecule
that encodes genetic information for living organisms. DNA is made up of four kinds of
nucleotides, which are molecules that bond together to form DNA sequences.

The four nucleotides are adenine (A), guanine (G), cytosine (C), and thymine (T). Each
strand of DNA is a sequence of nucleotides, for example AGCTAC. In a program, we will
use a string representation of this, 'AGCTAC'.

DNA has 2 strands in a double helix. The nucleotides in one strand are bonded to the
nucleotides in the other strand. A and T can be bonded together, and thus complement each
other; similarly, C and G are complements of each other.

You can see a picture of this on the Wikipedia page for DNA (https://en.wikipedia.org/wiki/DNA).
The two strands in DNA are complementary because each nucleotide in one strand is bonded with
its complement in the other strand. Thus, given the DNA sequence ACGTACG, its complementary
strand is TGCATGC.

Terminology in this assignment:
A DNA sequence is a sequence of nucleotides, such as TCATGT.
"""

import logging as log
import re


def is_valid_nucleotide(nucleotide):
    """ (str) -> bool

    Validate if 'nucleotide' is one of the for kinds of nucleotides, A, T, C, and G.
    Return True or False.

    >>> is_valid_nucleotide('A')
    True
    >>> is_valid_nucleotide('a')
    False
    >>> is_valid_nucleotide('X')
    False
    >>> is_valid_nucleotide('ACGTACG')
    False
    """
    # Validate if input can be processed as a string.
    try:
        nucleotide = str(nucleotide)
    except TypeError as err:
        log.info(err)
        return False

    regex = "^[ATCG]$"
    match = re.match(regex, nucleotide)
    if match is None:
        logtxt = (
            # Can't use f-string: autograder is python 3.5.
            #pylint: disable-next=consider-using-f-string
            "Invalid input: '{}'. ".format(nucleotide)
            + "Input should only contain one of the for kinds of nucleotides, A, T, C, and G."
        )
        log.info(logtxt)

        return False
    else:
        return True


def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if 'dna' is a valid DNA sequence (that is, it contains no
    characters other than the for kinds of nucleotides A, T, C, and G, or a zero-length
    sequence).

    >>> is_valid_sequence('ACGTACG')
    True
    >>> is_valid_sequence('ACGTXYZ')
    False
    >>> is_valid_sequence('A')
    True
    >>> is_valid_sequence('')
    True
    """
    # Validate if input can be processed as a string.
    try:
        dna = str(dna)
    except TypeError as err:
        log.info(err)
        return False

    regex = "^[ATCG]*$"
    match = re.match(regex, dna)
    if match is None:
        logtxt = (
            # Can't use f-string: autograder is python 3.5.
            #pylint: disable-next=consider-using-f-string
            "Invalid input: '{}'. ".format(dna)
            + "Input should only contain the for kinds of nucleotides, A, T, C, and G."
        )
        log.info(logtxt)

        return False
    else:
        return True


def get_length(dna):
    """ (str) -> int

    The parameter 'dna' is a DNA sequence. Return the length of that sequence.

    Pre-condition: 'dna' only contains the for kinds of nucleotides, A, T, C, and G.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    is_valid_sequence(dna)

    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    Pre-condition: both 'dna1' and 'dna2' only contain the for kinds of nucleotides, A, T, C, and G.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    is_valid_sequence(dna1)
    is_valid_sequence(dna2)

    return get_length(dna1) > get_length(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of 'nucleotide' in the DNA sequence 'dna'.

    Pre-condition: 'dna' only contains the for kinds of nucleotides, A, T, C, and G.
    'nucleotide' is one the for kinds of nucleotides, A, T, C, and G.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    is_valid_sequence(dna)
    is_valid_nucleotide(nucleotide)

    # Can't use f-string: autograder is python 3.5.
    #pylint: disable-next=consider-using-f-string
    regex = "[{}]".format(nucleotide)
    return len([*re.finditer(regex, dna)])



def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'G')
    True
    >>> contains_sequence('ATCGGC', 'ATC')
    True
    >>> contains_sequence('ATCGGC', 'TG')
    False

    """
    is_valid_sequence(dna1)
    is_valid_sequence(dna2)

    return dna1.find(dna2) != -1


def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    'dna1' and 'dna2' are DNA sequences and 'index' is an index.
    Return the DNA sequence obtained by inserting the second DNA sequence
    into the first DNA sequence at the given index.

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('CCATGG', 'A', 5)
    'CCATGAG'
    >>> insert_sequence('CCATGG', 'ATCG', 0)
    'ATCGCCATGG'
    """
    is_valid_sequence(dna1)
    is_valid_sequence(dna2)

    new_sequence = (
        dna1[:index]
        + dna2
        + dna1[index:]
    )
    return new_sequence


def get_complement(nucleotide):
    """ (str) -> str

    Return the nucleotide's complement of 'nucleotide'.
    (A and T complement each other; and C and G are complements of each other.)

    Pre-condition: 'nucleotide' is one the for kinds of nucleotides, A, T, C, and G.

    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    'G'
    >>> get_complement('G')
    'C'
    """
    is_valid_nucleotide(nucleotide)

    # Only available from pthon 3.10 onwards!
    #match nucleotide:
    #    case 'A':
    #        return "T"
    #    case 'T':
    #        return "A"
    #    case 'C':
    #        return "G"
    #    case 'G':
    #        return "C"

    if nucleotide == 'A':
        return "T"
    elif nucleotide == 'T':
        return "A"
    elif nucleotide == 'C':
        return "G"
    elif nucleotide == 'G':
        return "C"


def get_complementary_sequence(dna):
    """ (str) -> str

    Return the DNA sequence that is complementary to the given DNA sequence 'dna'.

    Pre-condition: 'dna' only contains the for kinds of nucleotides, A, T, C, and G.

    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('CCATGG')
    'GGTACC'
    >>> get_complementary_sequence('A')
    'T'
    """
    is_valid_sequence(dna)

    complementary_sequence = ''
    for nucleotide in dna:
        complementary_sequence += get_complement(nucleotide)

    return complementary_sequence
