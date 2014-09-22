#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors.
What is the first of these numbers?
'''


import math
import timeit


primes = [2, 3, 5, 7]


def prime_factorization(n):
    ps = []
    while True:
        n, p = factorize(n)
        if p == 1:
            if n != 1:
                ps.append(n)
            return ps
        ps.append(p)


def factorize(n):
    for p in primes:
        if n % p == 0:
            return n/p, p
    for i in range(2, int(math.sqrt(n/2))+1):
        if n % i == 0:
            primes.append(i)
            return n/i, i
    return n, 1


def loop(n):
    i = 0
    c = 0
    while True:
        i += 1
        ps = prime_factorization(i)
        if len(set(ps)) == n:
            c += 1
            if c == n:
                return i-n+1
        else:
            c = 0


if __name__ == '__main__':
    print loop(4)
    print timeit.Timer('problem_047.loop(4)', 'import problem_047').timeit(1)
