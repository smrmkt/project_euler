#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for
the consecutive values n = 0 to 39.
However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is
divisible by 41, and certainly when n = 41, 41² + 41 + 41 is
clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b,
for the quadratic expression that produces the maximum number of
primes for consecutive values of n, starting with n = 0.
'''

import math
import timeit


def loop(i):
    (ma, mb, mn) = (0, 0, 0)
    primes = [j for j in range(-i+1, i) if is_prime(abs(j))]
    for a in primes:
        for b in primes:
            n = 0
            while is_prime(n**2+a*n+b):
                n += 1
            (ma, mb, mn) = (a, b, n) if mn < n else (ma, mb, mn)
    return ma, mb, mn, ma*mb


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    print loop(1000)
    print timeit.Timer('problem_027.loop(1000)', 'import problem_027').timeit(1)