#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
'''

import timeit


def loop(n):
    chars = str(2**n)
    return sum([int(chars[i]) for i in range(len(chars))])

if __name__ == '__main__':
    print loop(1000)
    print timeit.Timer('problem_016.loop(1000)', 'import problem_016').timeit(10)
