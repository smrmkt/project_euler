#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
There are exactly ten ways of selecting three from five, 12345:
123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
In combinatorics, we use the notation, 5C3 = 10.
In general,

nCr =
n!
r!(n−r)!
,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr,
for 1 ≤ n ≤ 100, are greater than one-million?
'''

from math import factorial
import timeit


def calc(nlim, lim):
    cnt = 0
    for n in range(nlim+1):
        for r in range(n+1):
            ncr = factorial(n)/(factorial(r)*factorial(n-r))
            if ncr > lim:
                cnt += 1
    return cnt


if __name__ == '__main__':
    print calc(100, 1000000)
    print timeit.Timer('problem_053.calc(100, 1000000)', 'import problem_053').timeit(1)
