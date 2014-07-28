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

# slow
def loop(n):
    for a in range(1, int(n/3)):
        for b in range(a, int(n/2)):
            c = n - (a + b)
            if a + b < c:
                continue
            elif a**2 + b**2 == c**2:
                return a, b, c
    return None

if __name__ == '__main__':
    print loop(10000)
    print timeit.Timer('problem_009.loop(1000)', 'import problem_009').timeit(10)
