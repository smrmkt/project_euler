#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

from math import factorial
import timeit


def calc(digit, order):
    order -= 1
    facts = [factorial(i) for i in range(digit-1, 0, -1)]
    divs = get_divisors(facts, order)
    digits = map(str, range(0, digit))
    return get_ordered(digits, divs)


def get_divisors(facts, order):
    divs = []
    for f in facts:
        divs.append(int(order/f))
        order %= f
    return divs


def get_ordered(digits, divs):
    s = ''
    last_div = divs[-1]
    divs.pop(-1)
    for p in divs:
        s += digits[p]
        digits.pop(p)
    return s + digits[last_div] + digits[1-last_div]


if __name__ == '__main__':
    print calc(10, 1000000)
    print timeit.Timer('problem_024.calc(10, 1000000)', 'import problem_024').timeit(10)
