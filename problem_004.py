#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

import timeit

def loop(min, max):
    max_pal = 0;
    for i in range(max, min, -1):
        for j in range(i, min, -1): # by starting i, avoid duplicate multiplication
            if is_palindromic(i*j):
                max_pal = i*j if i*j > max_pal else max_pal
    return max_pal

def is_palindromic(n):
    s = str(n)
    return True if s == s[::-1] else False

if __name__ == '__main__':
    print loop(100, 999)
    print timeit.Timer('problem_004.loop(100, 999)', 'import problem_004').timeit(10)
