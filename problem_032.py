#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
'''

import timeit


def calc():
    pandigital = set()
    for i in range(1, 10000):
        for j in range(i, int(10000/i)+1):
            if ''.join(sorted(list(str(i) + str(j) + str(i*j)))) == '123456789':
                pandigital.add(i*j)
    return sum(pandigital)

if __name__ == '__main__':
    print calc()
    print timeit.Timer('problem_032.calc()', 'import problem_032').timeit(1)
