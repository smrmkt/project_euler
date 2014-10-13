#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
The cube, 41063625 (3453), can be permuted to produce two other cubes:
56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube
which has exactly three permutations of its digits which are also cube.
Find the smallest cube for which exactly five permutations of its digits are cube.
'''

import timeit


def calc(n):
    cubes = {}
    i = 1
    while True:
        s = ''.join(sorted(list(str(i**3))))
        cubes[s] = cubes.setdefault(s, [])+[i]
        if len(cubes[s]) == n:
            return cubes[s], min(cubes[s]), (min(cubes[s]))**3
        i += 1

if __name__ == '__main__':
    print calc(5)
    print timeit.Timer('problem_062.calc(5)', 'import problem_062').timeit(1)
