#!/usr/bin/env python
#-*-coding:utf-8-*-

'''

'''

import math
import timeit

primes = set()
compos = set()

def loop(n):
    truncatables = []
    for i in range(10, n):
        if '0' in set(str(i)):
            continue
        if cut_left(i)+cut_right(i) == 0:
            truncatables.append(i)
    return sum(truncatables)


def cut_right(n):
    if int(math.log10(n)) == 0:
        return 0 if n in [2, 3, 5, 7] else 1
    return is_not_prime(n)+cut_right(n/10)


def cut_left(n):
    l10 = int(math.log10(n))
    if l10 == 0:
        return 0 if n in [2, 3, 5, 7] else 1
    return is_not_prime(n)+cut_left(n%(10**int(math.log(n,10))))


def is_not_prime(n):
    if n in primes: return 0
    if n in compos: return 1
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            compos.add(n)
            return 1
    primes.add(n)
    return 0

if __name__ == '__main__':
    print loop(1000000)
    print timeit.Timer('problem_037.loop(1000000)', 'import problem_037').timeit(1)
