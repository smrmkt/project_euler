#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
'''

import timeit


class Poker:
    def __init__(self, cards):
        self.numbers = {}
        self.suits = {}
        for card in cards:
            n = self._to_number(card[0])
            s = card[1]
            self.numbers[n] = self.numbers.get(n, 0)+1
            self.suits[s] = self.suits.get(s, 0)+1

    def hand(self):
        n_max, n_min, n_len = max(self.numbers), min(self.numbers), len(self.numbers)
        sames = max(self.numbers.values())
        s_len = len(self.suits)
        n_diff = n_max-n_min
        if n_len == 5:
            if n_diff > 4:
                if s_len == 1: return 5 # flush
                else: return 0          # high card
            elif s_len > 1: return 4    # straight
            elif n_min == 10: return 9  # royal straight flush
            else: return 8              # straight flush
        elif n_len == 4: return 1       # one pair
        elif n_len == 3:
            if sames == 3: return 3     # three cards
            else: return 2              # two pair
        elif n_len == 2:
            if sames == 4: return 7     # four cards
            else: return 6              # full house

    def rank(self):
        s = ''
        for k,v in sorted(self.numbers.items(), key=lambda (k, v): (v, k), reverse=True):
            s += "{0:0>2}".format(str(k))*v
        return s

    def _to_number(self, s):
        s = str(s).replace('T', '10').replace('J', '11')\
            .replace('Q', '12').replace('K', '13').replace('A', '14')
        return int(s)


def calc():
    wins = [0]*3
    for line in open('data/problem_054.txt', 'r').readlines():
        cards = line.split(' ')
        p1 = Poker([card.rstrip() for card in cards[:5]])
        p2 = Poker([card.rstrip() for card in cards[5:]])
        if p1.hand() > p2.hand(): wins[0] += 1
        elif p1.hand() < p2.hand(): wins[2] += 1
        else:
            if p1.rank() > p2.rank(): wins[0] += 1
            elif p1.rank() < p2.rank(): wins[2] += 1
            else: wins[1] += 1
    return wins


if __name__ == '__main__':
    print calc()
    # print timeit.Timer('problem_030.calc(5)', 'import problem_030').timeit(1)
