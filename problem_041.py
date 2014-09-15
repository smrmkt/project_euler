#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
'''

import math
import timeit


def loop(n):
    for i in range(n, 1, -1):
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
    if len(set(list(str(n)))) == len(str(n)):
        return True
    return False

if __name__ == '__main__':
    print loop(7654321)
    print timeit.Timer('problem_041.loop(7654321)', 'import problem_041').timeit(1)
