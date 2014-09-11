#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
If p is the perimeter of a right angle triangle
with integral length sides, {a,b,c},
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

import timeit

def loop(n):
    max_p, max_num = 0, 0
    for p in range(12, n+1):
        num = pythagorean(p)
        if num > max_num:
            max_p, max_num = p, num
    return max_p

def pythagorean(n):
    count = 0
    for a in range(1, int(n/3)):
        for b in range(a, int(n/2)):
            c = n - (a + b)
            if a + b < c:
                continue
            elif a**2 + b**2 == c**2:
                count += 1
    return count

if __name__ == '__main__':
    print loop(1000)
    # print timeit.Timer('problem_039.loop(1000)', 'import problem_039').timeit(1)
