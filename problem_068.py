#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6,
and each line adding to nine.
Working clockwise, and starting from the group of three
with the numerically lowest external node (4,3,2 in this example),
each solution can be described uniquely.
For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12.
There are eight solutions in total.

Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6
By concatenating each group it is possible to form 9-digit strings;
the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements,
it is possible to form 16- and 17-digit strings.
What is the maximum 16-digit string for a "magic" 5-gon ring?
'''

import itertools
import timeit


def is_correct(outer, inner):
    total = (sum(outer)+sum(inner)*2)/5
    if outer[0]+inner[0]+inner[1] != total: return False
    if outer[1]+inner[1]+inner[2] != total: return False
    if outer[2]+inner[2]+inner[3] != total: return False
    if outer[3]+inner[3]+inner[4] != total: return False
    if outer[4]+inner[4]+inner[0] != total: return False
    return True


def concat(outer, inner):
    outer, inner = map(str, outer), map(str, inner)
    return int(outer[0]+inner[0]+inner[1]+
               outer[1]+inner[1]+inner[2]+\
               outer[2]+inner[2]+inner[3]+\
               outer[3]+inner[3]+inner[4]+\
               outer[4]+inner[4]+inner[0])


def loop():
    for i in range(6, 4, -1):
        strings = []
        for outer_elements in itertools.permutations(range(i+1, 11), 4):
            if 10 not in outer_elements:
                continue
            outer = [i]+list(outer_elements)
            inner_elements = [n for n in range(1, 11) if n not in outer]
            for inner_tuple in itertools.permutations(inner_elements):
                inner = list(inner_tuple)
                if is_correct(outer, inner):
                    strings.append(concat(outer, inner))
        if len(strings) > 0:
            return max(strings)


if __name__ == '__main__':
    print loop()
    print timeit.Timer('problem_068.loop()', 'import problem_068').timeit(1)
