#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
'''

import timeit


def calc(n):
     return sum([i for i in range(2, 9**n*10) if i == sum(map(lambda x: int(x)**n, list(str(i))))])

if __name__ == '__main__':
    print calc(5)
    print timeit.Timer('problem_030.calc(5)', 'import problem_030').timeit(1)
