#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.
Find the value of d < 1000 for which 1/d contains the longest
recurring cycle in its decimal fraction part.
'''

from math import sqrt
import timeit


def loop(n):
    max_d, max_r = 0, 0
    for i in range(6, n):
        if is_prime(i):
            divs = get_divisors(i-1)
            r = get_recurring_period(divs, i)
            if r > max_r:
                max_d, max_r = i, r
    return max_d


def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def get_divisors(n):
    d = []
    for i in range(1, int(sqrt(n)+1)):
        if i*i == n:
            d.append(i)
        elif n % i == 0:
            d.append(i)
            d.append(n/i)
    d.sort()
    return d

def get_recurring_period(divs, i):
    for d in divs:
        if (10**d-1) % i == 0:
            return d
    return None


if __name__ == '__main__':
    print loop(1000)
    print timeit.Timer('problem_026.loop(1000)', 'import problem_026').timeit(10)
