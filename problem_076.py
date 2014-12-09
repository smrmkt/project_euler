#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
'''

import timeit


def memoize(f):
    cache = {}
    def helper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return helper


@memoize
def p(k, n):
    if k > n:
        return 0
    elif k == n:
        return 1
    return p(k+1, n)+p(k, n-k)


def calc(n):
    return sum([p(k, n-k) for k in range(1, int(n/2)+1)])

if __name__ == '__main__':
    print calc(100)
    print timeit.Timer('problem_076.calc(100)', 'import problem_076').timeit(1)
