#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
The number, 197, is called a circular prime because
all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

import math
import timeit

def loop(n):
    circulars = []
    for i in range(2, n):
        if i not in circulars and '0' not in set(str(i)):
            c = get_circulars(i, len(str(i)))
            if len(str(i)) == len(c):
                circulars.extend(c)
    return len(set(circulars))

def get_circulars(n, l):
    ret = []
    if is_prime(n):
        ret.append(n)
    if l == 1:
        return ret
    else:
        s = str(n)
        return ret+get_circulars(int(s[-1]+s[:-1]), l-1)

def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    print loop(1000000)
    print timeit.Timer('problem_035.loop(1000000)', 'import problem_035').timeit(1)
