#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.
The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.
Which prime, below one-million, can be written as the sum of the most consecutive primes?
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


def calc(n):
    for i in range(2, n/10):
        if is_prime(i):
            primes.append(i)
    for i in range(len(primes)/10, 1, -1):
        if i % 100 == 0: print i
        for j in range(len(primes)-i):
            t = sum(primes[j:j+i])
            if t < n and is_prime(t):
                return t


if __name__ == '__main__':
    print calc(1000000)
    print timeit.Timer('problem_050.calc()', 'import problem_050').timeit(1)
