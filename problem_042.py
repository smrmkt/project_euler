#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
The nth term of the sequence of triangle numbers is given by,
tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number
corresponding to its alphabetical position and
adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'),
a 16K text file containing nearly two-thousand common English words,
how many are triangle words?
'''

import timeit


def calc(n):
    triangles = [i*(i+1)/2 for i in range(1, n+1)]
    words = [word[1:-1] for word in open('data/problem_042.txt', 'r').read().split(',')]
    return sum([1 if sum(ord(w)-64 for w in list(word)) in triangles else 0 for word in words])


if __name__ == '__main__':
    print calc(100)
    print timeit.Timer('problem_042.calc(30)', 'import problem_042').timeit(1)
