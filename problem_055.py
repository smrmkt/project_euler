#!/usr/bin/env python
#-*-coding:utf-8-*-

'''

'''

import timeit


def loop(n, m):
    return len([i for i in range(10, n) if not is_palindromic(i, m)])


def is_palindromic(n, m):
    if m == 0:
        return False
    else:
        s = str(n+int(str(n)[::-1]))
        diff = [i for i in range(int(len(s)/2)) if s[i] != s[-i-1]]
        if len(diff) > 0:
            return is_palindromic(int(s), m-1)
        else:
            return True


if __name__ == '__main__':
    print loop(10000, 50)
    print timeit.Timer('problem_055.loop(10000, 50)', 'import problem_055').timeit(1)
