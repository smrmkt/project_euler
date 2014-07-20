#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

import timeit

# slow
# simple loop
def loop(n):
    t = 0
    for i in range(1, n+1):
        if i % 3 == 0 or i % 5 == 0:
            t += i
    return t

# fast
# calculate each numbers' sum and subtract common multiplier
def calc(n):
    t03 = 3*(n/3)*(n/3+1)/2
    t05 = 5*(n/5)*(n/5+1)/2
    t15 = 15*(n/15)*(n/15+1)/2
    return t03 + t05 - t15

if __name__ == '__main__':
    print loop(999)
    print calc(999)
    print timeit.Timer('problem_001.loop(999)', 'import problem_001').timeit(100)
    print timeit.Timer('problem_001.calc(999)', 'import problem_001').timeit(100)
