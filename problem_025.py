#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
The Fibonacci sequence is defined by the recurrence relation:
Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144

The 12th term, F12, is the first term to contain three digits.
What is the first term in the Fibonacci sequence to contain 1000 digits?
'''

import timeit


def loop(order):
    f1 = 1
    f2 = 1
    cnt = 2
    while len(str(f2)) < order:
        f1, f2 = fibonacchi(f1, f2)
        cnt += 1
    return cnt


def fibonacchi(f1, f2):
    return f2, f1+f2


if __name__ == '__main__':
    print loop(1000)
    print timeit.Timer('problem_025.loop(1000)', 'import problem_025').timeit(10)
