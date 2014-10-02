#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.
Although no one has proved it yet, it is thought that some numbers,
like 196, never produce a palindrome.
A number that never forms a palindrome through the reverse and add process is
called a Lychrel number. Due to the theoretical nature of these numbers,
and for the purpose of this problem, we shall assume that a number is Lychrel
until proven otherwise. In addition you are given that
for every number below ten-thousand, it will either (i) become a palindrome
in less than fifty iterations, or, (ii) no one, with all the computing power that exists,
has managed so far to map it to a palindrome.
In fact, 10677 is the first number to be shown to require over fifty iterations
before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).
Surprisingly, there are palindromic numbers that are themselves Lychrel numbers;
the first example is 4994.
How many Lychrel numbers are there below ten-thousand?
NOTE: Wording was modified slightly on 24 April 2007 to emphasise
the theoretical nature of Lychrel numbers.
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
