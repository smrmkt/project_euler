#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
The primes 3, 7, 109, and 673, are quite remarkable.
By taking any two primes and concatenating them in any order
the result will always be prime. For example,
taking 7 and 109, both 7109 and 1097 are prime.
The sum of these four primes, 792, represents the lowest sum
for a set of four primes with this property.

Find the lowest sum for a set of five primes for which
any two primes concatenate to produce another prime.
'''

import math
import timeit


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def next_prime(n):
    while True:
        n += 1
        if is_prime(n):
            return n


def can_join(a, l):
    for b in l:
        if not is_prime(int(str(a)+str(b))):
            return False
        if not is_prime(int(str(b)+str(a))):
            return False
    return True


def calc(n, l=[], p=0):
    if len(l) >= n:
        return l
    while p < 10000:
        p = next_prime(p)
        if can_join(p, l):
            l = calc(n, l+[p], p)
            if len(l) >= n:
                break
    else:
        l.pop()
    return l


if __name__ == '__main__':
    print calc(5)
    print timeit.Timer('problem_060.calc(5)', 'import problem_060').timeit(1)
