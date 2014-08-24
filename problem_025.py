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
F10 = 55x
F11 = 89
F12 = 144

The 12th term, F12, is the first term to contain three digits.
What is the first term in the Fibonacci sequence to contain 1000 digits?
'''

from problem_003 import Loop
import timeit


def loop(order):
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            Loop().is_prime()



if __name__ == '__main__':
    print loop(1000)
    print timeit.Timer('problem_025.loop(1000)', 'import problem_025').timeit(10)

    def is_prime(self, n):
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
