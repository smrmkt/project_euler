#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
An irrational decimal fraction is created
by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part,
find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

from operator import mul
import timeit


def calc(n):
    d = "0"
    i = 1
    while i <= n:
        d += str(i)
        i += 1
    l = [d[1], d[10], d[100], d[1000], d[10000], d[100000], d[1000000]]
    return reduce(mul, map(int, l))


if __name__ == '__main__':
    print calc(1000000)
    print timeit.Timer('problem_040.calc(1000000)', 'import problem_040').timeit(1)
