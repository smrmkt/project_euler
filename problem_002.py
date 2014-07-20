#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
Each new term in the Fibonacci sequence is generated by
adding the previous two terms. By starting with 1 and 2,
the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values
do not exceed four million, find the sum of the even-valued terms.
'''

import timeit
import numpy as np

# dynamic programming algorithm
def loop(n):
    t = 0
    f = 1
    l = 1
    while l < n:
        if f % 2 == 0:
            t += f
        new = f + l
        l = f
        f = new
    return t

# reduce calculation by the fact that even-valued item appears in the two intervals.
# see http://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form
def loop_matrix(n):
    t = 0
    m = np.array([[3, 2], [2, 1]]) # multiply [[1, 1], [1, 1]] two times
    f = np.array([2, 1]) # first even-valued and previous item
    while f[0] < n:
        if f[0] % 2 == 0:
            t += f[0]
        new = np.dot(m, f)
        f = new
    return t

if __name__ == '__main__':
    print loop(4000000)
    print loop_matrix(4000000)
    print timeit.Timer('problem_002.loop(4000000)', 'import problem_002').timeit(100)
    print timeit.Timer('problem_002.loop_matrix(4000000)', 'import problem_002').timeit(100)
