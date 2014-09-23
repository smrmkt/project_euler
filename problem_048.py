#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
'''

import timeit


def calc(n):
    return sum([i**i for i in xrange(1, n+1)]) % 10**10


if __name__ == '__main__':
    print calc(1000)
    print timeit.Timer('problem_048.calc(1000)', 'import problem_048').timeit(1)
