#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
2520 is the smallest number that can be divided by
each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
'''

import math
import timeit

def loop(n):
    factors = [0] * (n+1)
    for i in range(1, n+1):
        tmp = factorize(i, [0] * (n+1))
        factors = [f if f > t else t for (f, t) in zip(factors, tmp)]
    t = 1
    for i, f in enumerate(factors):
        if f > 0:
            t *= i**f
    return t

# factorize integer as a list
def factorize(n, l):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: # i is prime of n
            l[i] += 1
            return factorize(int(n/i), l)
    l[n] += 1 # n is prime
    return l

if __name__ == '__main__':
    print loop(20)
    print timeit.Timer('problem_005.loop(20)', 'import problem_005').timeit(10)
