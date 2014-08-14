#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
'''

import timeit

alphabets = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E':5, 'F': 6, 'G': 7, 'H': 8,
    'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
    'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22,
    'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}

def calc():
    names = [name.replace('"', '')
             for name in open('data/problem_022.txt', 'r').read().split(',')]
    names.sort()
    t = 0
    for i in range(len(names)):
        t += (i+1) * get_alphabetical_order(names[i])
    return t

def get_alphabetical_order(name):
    t = 0
    for c in list(name):
        t += alphabets[c]
    return t

if __name__ == '__main__':
    print calc()
    print timeit.Timer('problem_022.calc()', 'import problem_022').timeit(10)
