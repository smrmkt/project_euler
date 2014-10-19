#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
The first ten continued fraction representations of (irrational) square roots are:

√2=[1;(2)], period=1
√3=[1;(1,2)], period=2
√5=[2;(4)], period=1
√6=[2;(2,4)], period=2
√7=[2;(1,1,1,4)], period=4
√8=[2;(1,4)], period=2
√10=[3;(6)], period=1
√11=[3;(3,6)], period=2
√12= [3;(2,6)], period=2
√13=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N ≤ 13, have an odd period.

How many continued fractions for N ≤ 10000 have an odd period?
'''

import math
import timeit


def make_proper(x, m, n):
    a = int(math.sqrt(x)+m)/n
    m -= a*n
    return a, m


def inverse_rationalize(x, m, n):
    n = (x-m**2)/n
    return n, -m


def calc(x, m, n):
    pairs = []
    while True:
        a, m = make_proper(x, m, n)
        n, m = inverse_rationalize(x, m, n)
        if [a, n, m] in pairs:
            return pairs[1:]
        else:
            pairs.append([a, n, m])


def loop(n):
    odd_period = 0
    for i in range(1, n+1):
        if math.sqrt(i) == int(math.sqrt(i)):
            continue
        if len(calc(i, 0, 1))%2 == 1:
            odd_period += 1
    return odd_period


if __name__ == '__main__':
    print loop(10000)
    print timeit.Timer('problem_064.loop(10000)', 'import problem_064').timeit(1)
