#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
It is possible to write ten as the sum of primes
in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as
the sum of primes in over five thousand different ways?
'''

import math
import timeit


primes = [2]


def is_prime(n):
    for p in primes:
        if n % p == 0:
            return False
    for i in range(max(primes)+1, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def next_prime(n):
    return filter(lambda x: x > n, primes)[0]


def memoize(f):
    cache = {}
    def helper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return helper


@memoize
def p(k, n):
    if k > n:
        return 0
    elif k == n:
        return 1
    return p(next_prime(k), n)+p(k, n-k)


def calc(lim):
    for i in range(2, lim):
        if is_prime(i):
            primes.append(i)
    for n in range(2, lim):
        primes_in_range = [i for i in primes if i < int(n/2)+1]
        total = sum([p(k, n-k) for k in primes_in_range])
        if total > lim:
            return n, total


if __name__ == '__main__':
    print calc(5000)
    print timeit.Timer('problem_077.calc(5000)', 'import problem_077').timeit(1)
