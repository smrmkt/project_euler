#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
'''

import math
import timeit


def is_pentagonal(n):
    if (1+math.sqrt(1+24*n)) % 6 == 0:
        return True
    else:
        return False


def calc():
    i = 143
    while True:
        i += 1
        n = i*(2*i-1)
        if is_pentagonal(n):
            return n


if __name__ == '__main__':
    print calc()
    print timeit.Timer('problem_045.calc()', 'import problem_045').timeit(1)
