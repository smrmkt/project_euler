#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
It can be seen that the number, 125874, and its double, 251748,
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x,
such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

import timeit


def loop(n):
    for i in range(10, 10000000):
        if str(i)[0] != '1':
            continue
        f = [1 for j in range(2, n+1) if sorted(list(str(i))) != sorted(str(i*j))]
        if len(f) == 0:
            return i


if __name__ == '__main__':
    print loop(6)
    print timeit.Timer('problem_052.loop(6)', 'import problem_052').timeit(1)
