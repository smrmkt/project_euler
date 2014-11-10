#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
Consider quadratic Diophantine equations of the form:

x2 – Dy2 = 1

For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.
It can be assumed that there are no solutions in positive integers when D is square.
By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

32 – 2×22 = 1
22 – 3×12 = 1
92 – 5×42 = 1
52 – 6×22 = 1
82 – 7×32 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.
Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
'''

import math
import timeit

# very slow
def solve(d):
    x = 2.0
    while True:
        a = (x**2-1)/d
        if a == int(a):
            b = math.sqrt(a)
            if b == int(b):
                return int(x)
        x += 1.0


# pell equation
# http://www.asahi-net.or.jp/~kc2h-msm/excel/excel002.htm
def pell(d):
    P = 0
    Q = 1
    a1 = int(math.sqrt(d))
    a = a1
    p = [a, 1]
    q = [1, 0]
    while True:
        P = a*Q-P
        Q = (d-P**2)/Q
        a = int((a1+P)/Q)
        p = [a*p[0]+p[1], p[0]]
        q = [a*q[0]+q[1], q[0]]
        if p[0]**2-d*(q[0]**2) == 1:
            return p[0]


def loop(n):
    max_d, max_x = 0, 0
    for d in range(2, n+1):
        if math.sqrt(d) == int(math.sqrt(d)):
            continue
        else:
            x = pell(d)
            if x > max_x:
                max_d, max_x = d, x
    return max_d, max_x


if __name__ == '__main__':
    print loop(1000)
    print timeit.Timer('problem_066.loop(1000)', 'import problem_066').timeit(1)
