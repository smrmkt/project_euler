#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
 Consider the fraction, n/d, where n and d are positive integers.
 If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?
'''

import math
import timeit


def factorize(n, factors):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            factors.add(i)
            return factorize(int(n/i), factors)
    factors.add(n)
    return factors


def proper_fractions(n, factors):
    cnt = 0
    for i in range(1, n+1):
        if float(i)/n <= 1.0/3 or 1.0/2 <= float(i)/n:
            continue
        divs = [i%factor for factor in factors]
        if not 0 in divs:
            cnt += 1
    return cnt


def loop(n):
    cnt = 0
    for i in range(1, n+1):
        factors = factorize(i, set())
        cnt += proper_fractions(i, factors)
    return cnt

if __name__ == '__main__':
    print loop(12000)
    print timeit.Timer('problem_073.loop(12000)', 'import problem_073').timeit(1)
