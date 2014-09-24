#!/usr/bin/env python
#-*-coding:utf-8-*-

'''

'''

from itertools import permutations
import math
import timeit


def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def calc():
    seqs = []
    for i in range(1000, 9999):
        if not is_prime(i): continue
        perms = list(set([int(''.join(s)) for s in permutations(str(i), 4)]))
        perms.sort()
        for j in range(0, len(perms)):
            if perms[j] < i: continue
            if not is_prime(perms[j]): continue
            for k in range(j, len(perms)):
                if not is_prime(perms[k]): continue
                if (perms[j]-i)*2 == perms[k]-i and perms[k]-i > 0:
                    seqs.append(''.join(map(str, [i, perms[j], perms[k]])))
    return seqs


if __name__ == '__main__':
    print calc()
    print timeit.Timer('problem_049.calc()', 'import problem_049').timeit(1)
