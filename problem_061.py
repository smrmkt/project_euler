#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are
all figurate (polygonal) numbers and are generated by the following formulae:

Triangle	 	P3,n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Square	 	P4,n=n2	 	1, 4, 9, 16, 25, ...
Pentagonal	 	P5,n=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	P6,n=n(2n−1)	 	1, 6, 15, 28, 45, ...
Heptagonal	 	P7,n=n(5n−3)/2	 	1, 7, 18, 34, 55, ...
Octagonal	 	P8,n=n(3n−2)	 	1, 8, 21, 40, 65, ...

The ordered set of three 4-digit numbers: 8128, 2882, 8281,
has three interesting properties.

The set is cyclic, in that the last two digits of each number is
the first two digits of the next number (including the last number with the first).
Each polygonal type: triangle (P3,127=8128), square (P4,91=8281),
and pentagonal (P5,44=2882), is represented by a different number in the set.
This is the only set of 4-digit numbers with this property.
Find the sum of the only ordered set of six cyclic 4-digit numbers
for which each polygonal type: triangle, square, pentagonal, hexagonal,
heptagonal, and octagonal, is represented by a different number in the set.
'''

import itertools
import timeit

polygonal = [[], [], [], [], [], []]
for i in range(6):
    polygonal[i] = [n*((i+1)*n+(1-i))/2 for n in range(1, 200) if 1000 <= n*((i+1)*n+(1-i))/2 <= 10000]


def next_candidates(n, i):
    return [p for p in polygonal[i] if n/100 == p%100]


def cyclic(l, o, n):
    if len(l) == n:
        return l
    candidates = next_candidates(l[-1], o[len(l)])
    for c in candidates:
        l = cyclic(l+[c], o, n)
        if len(l) == n:
            break
    else:
        l.pop()
    return l


def calc(n):
    for o in itertools.permutations(range(n)):
        order = list(o)
        for i in polygonal[order[0]]:
            l = cyclic([i], order, n)
            if len(l) == n and l[0]%100 == l[-1]/100:
                return sum(l), l, o

if __name__ == '__main__':
    print calc(6)
    print timeit.Timer('problem_061.calc(6)', 'import problem_061').timeit(1)
