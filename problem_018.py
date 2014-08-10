#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
If the numbers 1 to 5 are written out in words:
one two three four five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were
written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
'''

import timeit

# not beautiful and inaccurate
class TriangleParts:
    def __init__(self):
        self.l, self.triangles = self.load_triangle('data/problem_018.txt')
        self.total = self.triangles[0]
        self.paths = [0] * self.l

    def loop(self):
        row = 0
        col = 0
        while row < self.l-1:
            update = 4 if self.l-row > 4 else self.l-row-1
            parts = self.get_triangle_parts(row*1000+col, update)
            path, value = self.get_maximum_path(parts, update)
            for i in range(update):
                self.paths[row+i+1] = int(path[i:i+1]) + col
            self.total += value
            row += update
            col += int(path) % 10
        return self.total

    def load_triangle(self, path):
        triangles = {}
        lines = open(path, 'r').readlines()
        for l in range(len(lines)):
            nums = lines[l].rstrip().split(' ')
            for n in range(len(nums)):
                triangles[l*1000+n] = int(nums[n])
        return l+1, triangles

    def get_triangle_parts(self, s, d):
        row = s / 1000
        col = s % 1000
        parts = {}
        for i in range(1, d+1):
            for j in range(i+1):
                parts[i*1000+j] = self.triangles[(row+i)*1000+col+j]
        return parts

    def get_maximum_path(self, parts, d):
        if d == 1:
            kvs = {
                '0':    parts[1000],
                '1':    parts[1001]
            }
        elif d == 2:
            kvs = {
                '00':   parts[1000]+parts[2000],
                '01':   parts[1000]+parts[2001],
                '11':   parts[1001]+parts[2001],
                '12':   parts[1001]+parts[2002]
            }
        elif d == 3:
            kvs = {
                '000':  parts[1000]+parts[2000]+parts[3000],
                '001':  parts[1000]+parts[2000]+parts[3001],
                '011':  parts[1000]+parts[2001]+parts[3001],
                '012':  parts[1000]+parts[2001]+parts[3002],
                '111':  parts[1001]+parts[2001]+parts[3001],
                '112':  parts[1001]+parts[2001]+parts[3002],
                '122':  parts[1001]+parts[2002]+parts[3002],
                '123':  parts[1001]+parts[2002]+parts[3003],
            }
        elif d == 4:
            kvs = {
                '0000': parts[1000]+parts[2000]+parts[3000]+parts[4000],
                '0001': parts[1000]+parts[2000]+parts[3000]+parts[4001],
                '0011': parts[1000]+parts[2000]+parts[3001]+parts[4001],
                '0012': parts[1000]+parts[2000]+parts[3001]+parts[4002],
                '0111': parts[1000]+parts[2001]+parts[3001]+parts[4001],
                '0112': parts[1000]+parts[2001]+parts[3001]+parts[4002],
                '0122': parts[1000]+parts[2001]+parts[3002]+parts[4002],
                '0123': parts[1000]+parts[2001]+parts[3002]+parts[4003],
                '1111': parts[1001]+parts[2001]+parts[3001]+parts[4001],
                '1112': parts[1001]+parts[2001]+parts[3001]+parts[4002],
                '1122': parts[1001]+parts[2001]+parts[3002]+parts[4002],
                '1123': parts[1001]+parts[2001]+parts[3002]+parts[4003],
                '1222': parts[1001]+parts[2002]+parts[3002]+parts[4002],
                '1223': parts[1001]+parts[2002]+parts[3002]+parts[4003],
                '1233': parts[1001]+parts[2002]+parts[3003]+parts[4003],
                '1234': parts[1001]+parts[2002]+parts[3003]+parts[4004]
            }
        return max(kvs.items(), key=lambda x: x[1])[0], max(kvs.values())

# dynamic programing
class DynamicProgramming:
    def __init__(self):
        self.n, self.triangle = self.load_triangle('data/problem_018.txt')

    def recursive(self, r):
        if r < 0:
            return self.triangle[0][0]
        else:
            for c in range(r+1):
                self.triangle[r][c] += max([self.triangle[r+1][c], self.triangle[r+1][c+1]])
            return self.recursive(r-1)

    def load_triangle(self, path):
        triangle = []
        lines = open(path, 'r').readlines()
        for l in range(len(lines)):
            triangle.append(map(int, lines[l].rstrip().split(' ')))
        return l+1, triangle

if __name__ == '__main__':
    print TriangleParts().loop()
    print DynamicProgramming().recursive(DynamicProgramming().n-2)
    print timeit.Timer('problem_018.TriangleParts().loop()',
                       'import problem_018').timeit(10)
    print timeit.Timer('problem_018.DynamicProgramming().recursive(problem_018.DynamicProgramming().n-2)',
                       'import problem_018').timeit(10)
