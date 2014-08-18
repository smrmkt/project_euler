#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
A perfect number is a number for which
the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is
less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that
all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be expressed
as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written
as the sum of two abundant numbers.
'''

from math import sqrt
import timeit

def get_divisor(n):
    d = [1]
    for i in range(2, int(sqrt(n)+1)):
        if i*i == n:
            d.append(i)
        elif n % i == 0:
            d.append(i)
            d.append(n/i)
    return d

def sum_of_two(n, a, c):
    for i in a:
        if i > n / 2:
            break
        if c[n - i]:
            return True
    return False

def calc(n):
    c = [False] * (n + 1)
    for i in range(1, n+1):
        if sum(get_divisor(i)) > i:
            c[i] = True
    a = [i for i in range(n+1) if c[i]]
    return sum([i for i in range(1, n+1) if not sum_of_two(i, a, c)])


if __name__ == '__main__':
    print calc(28123)
    print timeit.Timer('problem_023.calc(28123)', 'import problem_023').timeit(1)
