#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
Consider the fraction, n/d, where n and d are positive integers.
If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size,
find the numerator of the fraction immediately to the left of 3/7.
'''

from fractions import Fraction
import math
import timeit


primes = [2, 3, 5, 7]


def is_prime(n):
    for p in primes:
        if n % p == 0:
            return False
    for i in range(max(primes), int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def factorize(n, factors):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            factors.add(i)
            return factorize(int(n/i), factors)
    factors.add(n)
    return factors

def is_proper_fraction(num, den):
    factors = factorize(den, set())
    for factor in factors:
        if num%factor == 0:
            return False
    return True

def get_immediate_fraction(num, den, frac):
    if  frac < Fraction(num, den) and  is_proper_fraction(num, den):
        return Fraction(num, den)
    return frac

def loop(n):
    frac = Fraction(0, 1)
    for den in range(1, n+1):
        if den == 7:
            continue
        num = int(den*3/7)
        frac = get_immediate_fraction(num, den, frac)
    return frac


if __name__ == '__main__':
    print loop(1000000)
    print timeit.Timer('problem_071.loop(1000000)', 'import problem_071').timeit(1)
