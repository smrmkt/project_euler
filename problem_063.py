#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
The 5-digit number, 16807=75, is also a fifth power.
Similarly, the 9-digit number, 134217728=89, is a ninth power.
How many n-digit positive integers exist which are also an nth power?
'''

import timeit


def get_powers(n):
    i, t = 1, 0
    while True:
        l = len(str(i**n))
        if l == n:
            t += 1
        elif l > n:
            return t
        i += 1


def calc(n):
    powers = []
    for i in range(1, n):
        powers.append(get_powers(i))
    return sum(powers), powers


if __name__ == '__main__':
    print calc(100)
    print timeit.Timer('problem_063.calc(100)', 'import problem_063').timeit(1)
