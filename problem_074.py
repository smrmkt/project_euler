#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
The number 145 is well known for the property that
the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers
that link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop.
For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms,
but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million,
contain exactly sixty non-repeating terms?
'''

import math
import timeit

factorial = [math.factorial(i) for i in range(10)]


def sum_of_factorial(n):
    return sum([factorial[int(s)] for s in list(str(n))])


def count_chain(n):
    chain = [n]
    num = sum_of_factorial(n)
    while num not in chain:
        chain.append(num)
        num = sum_of_factorial(num)
    return len(chain)


def calc(n, rep):
    return len(filter(lambda i: i==rep, [count_chain(i) for i in range(1, n+1)]))


if __name__ == '__main__':
    print calc(1000000, 60)
    print timeit.Timer('problem_074.calc(1000000, 60)', 'import problem_074').timeit(1)
