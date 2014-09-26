#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
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
