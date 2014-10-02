#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
A googol (10100) is a massive number:
one followed by one-hundred zeros; 100100 is almost
unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.
Considering natural numbers of the form, ab,
where a, b < 100, what is the maximum digital sum?
'''

import timeit


def loop(n):
    return max([sum(map(int, list(str(pow(a, b))))) for a in range(n) for b in range(n)])


if __name__ == '__main__':
    print loop(100)
    print timeit.Timer('problem_056.loop(100)', 'import problem_056').timeit(1)
