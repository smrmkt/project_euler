#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
'''

import math
import timeit

def loop():
    for i in range(7654321, 1234567, -1):
        if is_pandigital(i):
            if is_prime(i):
                return i
    return None

def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def is_pandigital(n):
    if set(list(str(n))) == set(map(str, range(1, int(math.log10(n)+2)))):
        return True
    return False

if __name__ == '__main__':
    print loop()
    print timeit.Timer('problem_041.loop()', 'import problem_041').timeit(1)
