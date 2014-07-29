#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import numpy as np
import timeit
import problem_005

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

# Pythagorean theorem
def pythagorean(n):
    if n % 2 != 0: return None # n must be even
    for l in range(3, int(n/2)):
        if n/2 % l != 0: continue
        s = n/(2*l) - l
        if s < 0: continue
        lf = np.array(problem_005.factorize(l, [0]*n))
        sf = np.array(problem_005.factorize(s, [0]*n))
        if l > s and (l-s)%2 == 1 and np.dot(lf, sf) == 0: # lf and sf must be coprime
            print l, s
            return l**2-s**2, 2*l*s, l**2+s**2
    return None

if __name__ == '__main__':
    print loop(1000)
    print pythagorean(1000) # None because 1000 is not consist of primitive pythagorean theorem
    print timeit.Timer('problem_009.loop(1000)', 'import problem_009').timeit(10)
    print timeit.Timer('problem_009.pythagorean(1000)', 'import problem_009').timeit(10)
