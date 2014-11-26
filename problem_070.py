#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
Euler's Totient function, φ(n) [sometimes called the phi function],
is used to determine the number of positive numbers less than or equal to n
which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and
the ratio n/φ(n) produces a minimum.
'''

from fractions import Fraction
import itertools
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


def totient(n):
    factors = factorize(n, set())
    return n*reduce(lambda x,y: x*y, map(lambda x: 1-Fraction(1, x), factors))


# slow
def loop(n):
    num, min_ratio = None, None
    for i in range(2, n+1):
        phi = totient(i)
        if sorted(str(i)) == sorted(str(phi)):
            ratio = n/phi
            if min_ratio is None or ratio < min_ratio:
                num = i
                min_ratio = ratio
    return num, min_ratio


def multiple_prime(n):
    # prepare primes
    for i in range(1000, 5000): # narrow search space
        if is_prime(i):
            primes.append(i)
    # main loop
    num, min_ratio = None, None
    for i, j in itertools.combinations(primes, 2):
        m = i*j
        if m > n:
            continue
        phi = totient(m)
        if sorted(str(m)) == sorted(str(phi)):
            ratio = m/phi
            if min_ratio is None or ratio < min_ratio:
                num = m
                min_ratio = ratio
    return num, min_ratio


if __name__ == '__main__':
    # print loop(10**7)
    print multiple_prime(10**7)
    print timeit.Timer('problem_070.multiple_prime(10**7)', 'import problem_070').timeit(1)
