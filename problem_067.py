#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
By starting at the top of the triangle below and
moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt
(right click and 'Save Link/Target As...'),
a 15K text file containing a triangle with one-hundred rows.
'''

import timeit


def load_triangle():
    triangle = []
    for line in open('data/problem_067.txt', 'r').readlines():
        triangle.append(map(int, line.split(' ')))
    return triangle


# using Dynamic Programming
def calc():
    tr = load_triangle()
    for r in range(len(tr)-2, -1, -1):
        for c in range(r+1):
            tr[r][c] += max([tr[r+1][c], tr[r+1][c+1]])
    return tr[0]


if __name__ == '__main__':
    print calc()
    print timeit.Timer('problem_067.calc()', 'import problem_067').timeit(1)
