#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe
that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
'''

from fractions import Fraction
from operator import mul
import timeit


def calc():
    fracs = {}
    for i in range(10, 100):
        if len(set(str(i))) == 1: continue
        for j in range(i, 100):
            if len(set(str(j))) == 1: continue
            if (str(i))[0] == (str(j))[1]:
                if float((str(i))[1])/float((str(j))[0]) == float(i)/j:
                    fracs[i] = j
            elif (str(i))[1] == (str(j))[0]:
                if (str(j))[1] == '0': continue
                if float((str(i))[0])/float((str(j))[1]) == float(i)/j:
                    fracs[i] = j
    return Fraction(reduce(mul, fracs.keys()), reduce(mul, fracs.values())).denominator


if __name__ == '__main__':
    print calc()
    print timeit.Timer('problem_033.calc()', 'import problem_033').timeit(10)
