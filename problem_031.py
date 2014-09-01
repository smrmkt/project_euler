#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
In England the currency is made up of pound, £, and pence,
p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

import timeit

# slow
def loop(total):
    cnt = 0
    for i in range(int(total/200)+1):
        for j in range(int(total/100)+1):
            for k in range(int(total/50)+1):
                for l in range(int(total/20)+1):
                    for m in range(int(total/10)+1):
                        for n in range(int(total/5)+1):
                            for o in range(int(total/2)+1):
                                if i*200+j*100+k*50+l*20++m*10+n*5+o*2 <= total:
                                    cnt += 1
    return cnt

# fast
def recursive(total, coins):
    if coins == [1]:
        return 1
    cnt = 0
    for i in range(0, int(total/coins[0])+1):
        cnt += recursive(total-coins[0]*i, coins[1:])
    return cnt


if __name__ == '__main__':
    print loop(200)
    print recursive(200, [200, 100, 50, 20, 10, 5, 2, 1])
    print timeit.Timer('problem_031.loop(200)', 'import problem_031').timeit(1)
    print timeit.Timer('problem_031.recursive(200, [200, 100, 50, 20, 10, 5, 2, 1])',
                       'import problem_031').timeit(1)
