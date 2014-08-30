#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
Surprisingly there are only three numbers that can be written
as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.
Find the sum of all the numbers that can be written
as the sum of fifth powers of their digits.
'''

import timeit


def calc(n):
     return sum([i for i in range(2, 9**n*10) if i == sum(map(lambda x: int(x)**n, list(str(i))))])

if __name__ == '__main__':
    print calc(5)
    print timeit.Timer('problem_030.calc(5)', 'import problem_030').timeit(1)
