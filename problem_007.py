#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

import timeit

def loop(n):
    p = 1
    l = []
    while len(l) < n:
        p, l = get_prime(p, l)
    return max(l)

def get_prime(p, l):
    while True:
        p += 1
        is_prime = True
        for i in l:
            if p % i == 0:
                is_prime = False
                break
        if is_prime is True:
            l.append(p)
            return p, l

if __name__ == '__main__':
    print loop(10001)
    print timeit.Timer('problem_007.loop(10001)', 'import problem_007').timeit(1)
