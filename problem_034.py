#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to
the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

import math
import timeit

def calc():
    eqs = []
    for i in range(3, 2177280):
        if i == sum(map(lambda j: math.factorial(j), map(int, list(str(i))))):
            eqs.append(i)
    return eqs

if __name__ == '__main__':
    print calc()
    print timeit.Timer('problem_034.calc()', 'import problem_034').timeit(1)
