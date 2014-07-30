#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

import math
import random

# simple loop
class Loop:
    def upto(self, n):
        if n < 2:
            return None
        for i in range(n, 2, -1):
            if self.is_prime(i):
                return i
        return None

    def is_prime(self, n):
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True

# Sieve of Eratosthenes
class Eratosthenes:
    def upto(self, n):
        if n < 2:
            return None
        else:
            return max(self.sieve(range(2, n)))

    def sieve(self, numbers):
        if len(numbers) == 1:
            return numbers
        else:
            head = numbers[0]
            return self.sieve([n for n in numbers[1:] if n % head != 0])

# Fermat's little theorem
# see http://en.wikipedia.org/wiki/Fermat's_little_theorem
class Fermat:
    def upto(self, n):
        if n < 2:
            return None
        for i in range(n, 2, -1):
            if self.is_prime(i):
                return i
        return None

    def is_prime(self, n):
        if n == 2:
            return True
        if n < 2 or n & 1 == 0:
            return False
        return pow(2, n-1, n) == 1

# Miller-Rabin primarity test
class MillerRabin:
    def upto(self, n, l=10):
        if n < 2:
            return None
        for i in range(n, 2, -1):
            if self.is_prime(i, l):
                return i
        return None

    def is_prime(self, n, l):
        if n == 2:
            return True
        if n < 2 or n & 1 == 0:
            return False
        # acquire d and s
        d = (n - 1) >> 1
        while d & 1 == 0:
            d >>= 1
        # check l times
        for i in xrange(l):
            a = random.randint(1, n-1)
            t = d
            y = pow(a, t, n)
            while t != n - 1 and y != 1 and y != n - 1:
                y = pow(y, 2, n)
                t <<= 1
            if y != n - 1 and t & 1 == 0:
                return False
        return True

if __name__ == '__main__':
    n = 1000
    print Loop().upto(n)
    print Eratosthenes().upto(n)
    print Fermat().upto(n)
    print MillerRabin().upto(n, 1)
