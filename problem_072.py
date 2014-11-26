#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
Consider the fraction, n/d, where n and d are positive integers.
If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.
How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?
'''

from fractions import Fraction
import math
import timeit


primes = [2]


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
        if i in primes and n % i == 0:
            factors.add(i)
            return factorize(int(n/i), factors)
    factors.add(n)
    return factors


def totient(n):
    if n % 10000 == 0:
        print n
    factors = factorize(n, set())
    return n*reduce(lambda x,y: x*y, map(lambda x: 1-Fraction(1, x), factors))


def calc(n):
    for i in range(3, int(math.sqrt(n)+1)):
        if is_prime(i):
            primes.append(i)
    return sum([totient(i) for i in range(1, n+1)])


if __name__ == '__main__':
    print calc(1000000)
    print timeit.Timer('problem_072.calc(10000000)', 'import problem_072').timeit(1)
