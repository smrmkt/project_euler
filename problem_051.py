#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
By replacing the 1st digit of the 2-digit number *3,
it turns out that six of the nine possible values:
13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit,
this 5-digit number is the first example having seven primes
among the ten generated numbers, yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family,
is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number
(not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.
'''

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


def replace(n, i):
    s = str(n)
    return [int(s.replace(i, str(j))) for j in range(10)]

def loop(n):
    for i in range(56993, 1000000):
        if is_prime(i):
            for j in set(str(i)):
                reps = [r for r in replace(i, j) if is_prime(r)]
                if len(reps) == n and len(str(i)) == len(str(min(reps))):
                    return min(reps)


if __name__ == '__main__':
    print loop(8)
    print timeit.Timer('problem_051.loop(8)', 'import problem_051').timeit(1)
