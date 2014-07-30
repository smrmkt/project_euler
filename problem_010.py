#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import timeit
import problem_003

# slow
def loop(n):
    t = 0
    for i in range(2, n):
        if problem_003.Loop().is_prime(i):
        # if problem_003.MillerRabin().is_prime(i, 10):
            t += i
    return t

# faster
def mr(n):
    t = 0
    for i in range(2, n):
        if problem_003.MillerRabin().is_prime(i, 3):
            t += i
    return t

if __name__ == '__main__':
    print loop(2000000)
    print mr(2000000)
    print timeit.Timer('problem_010.loop(2000000)', 'import problem_010').timeit(1)
    print timeit.Timer('problem_010.mr(2000000)', 'import problem_010').timeit(1)
