#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
The decimal number, 585 = 10010010012 (binary),
is palindromic in both bases.

Find the sum of all numbers, less than one million,
which are palindromic in base 10 and base 2.

(Please note that the palindromic number,
in either base, may not include leading zeros.)
'''

import timeit


def loop(n):
    palindromics = []
    for i in range(1, n+1):
        b = format(i, 'b')
        if is_palindromic(i) and is_palindromic(b):
            palindromics.append(i)
    return sum(palindromics)

def is_palindromic(n):
    nstr = str(n)
    rnstr = ''.join(list(nstr)[::-1])
    return nstr == rnstr

if __name__ == '__main__':
    print loop(1000000)
    print timeit.Timer('problem_036.loop(1000000)', 'import problem_036').timeit(1)
