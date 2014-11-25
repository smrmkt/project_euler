#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
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
