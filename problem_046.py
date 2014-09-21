#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
It was proposed by Christian Goldbach that every odd composite number
can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written
as the sum of a prime and twice a square?
'''


import math
import timeit


primes = []

def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def is_goldbach(n):
    for p in primes:
        for i in range(1, n):
            c = p+2*(i**2)
            if c == n:
                return True
            elif c > n:
                break
    return False


def calc():
    i = 0
    while True:
        i += 1
        if i % 2 == 0:
            continue
        elif is_prime(i):
            primes.append(i)
        elif is_goldbach(i):
            continue
        else:
            return i


if __name__ == '__main__':
    print calc()
    print timeit.Timer('problem_046.calc()', 'import problem_046').timeit(1)
