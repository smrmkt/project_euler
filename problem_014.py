#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

import timeit


def loop(n):
    max_num = 0
    max_cnt = 1
    for i in range(1, n):
        cnt = recursive(i, 0)
        if cnt > max_cnt:
            max_num = i
            max_cnt = cnt
    return max_num, max_cnt


def recursive(n, i):
    if n == 1:
        return i
    else:
        n = n / 2 if n % 2 == 0 else 3 * n + 1
        i += 1
        return recursive(n, i)

if __name__ == '__main__':
    print loop(1000000)
    print timeit.Timer('problem_014.loop(1000000)', 'import problem_014').timeit(1)
