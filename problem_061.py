#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
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
