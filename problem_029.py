#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
Starting with the number 1 and moving to the right
in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals
in a 1001 by 1001 spiral formed in the same way?
'''

import timeit


def calc(a, b):
    return len(set([i**j for i in range(2, a+1) for j in range(2, b+1)]))

if __name__ == '__main__':
    print calc(100, 100)
    print timeit.Timer('problem_029.calc(100, 100)', 'import problem_029').timeit(10)
