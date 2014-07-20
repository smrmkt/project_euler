#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

import timeit

def loop(min, max):
    max_pal = 0;
    for i in range(max, min, -1):
        for j in range(max, min, -1):
            if is_palindromic(i*j):
                max_pal = i*j if i*j > max_pal else max_pal
    return max_pal

def is_palindromic(n):
    s = str(n)
    return True if s == s[::-1] else False

if __name__ == '__main__':
    print loop(100, 999)
    print timeit.Timer('problem_004.loop(100, 999)', 'import problem_004').timeit(10)
