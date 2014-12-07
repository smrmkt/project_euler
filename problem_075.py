#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
It turns out that 12 cm is the smallest length of wire
that can be bent to form an integer sided right angle triangle in exactly one way,
but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form
an integer sided right angle triangle, and other lengths allow more than
one solution to be found;
for example, using 120 cm it is possible to form exactly three different integer
sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of
L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?
'''

import math
import timeit


def gcd(a, b):
    return b if  a%b == 0 else gcd(b, a%b)


def calc(lim):
    pytagoreans = []
    for m in range(1, int(math.sqrt(lim/2))+1):
        for n in range(1, m):
            if (m-n)%2 == 1 and gcd(m, n) == 1:
                pytagoreans.append(2*m*(m+n))
    sums = [0]*(lim+1)
    for p in pytagoreans:
        i = 1
        while p*i <= lim:
            sums[p*i] += 1
            i += 1
    return sum([s for s in sums if s == 1])


if __name__ == '__main__':
    print calc(1500000)
    print timeit.Timer('problem_075.calc(1500000)', 'import problem_075').timeit(1)
