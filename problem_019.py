#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
You are given the following information,
but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4,
but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during
the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

from math import floor
import timeit

# Zeller's congruence
class Zeller:
    def get_day_of_week(self, year, month, day):
        if 1 <= month <= 2:
            year -= 1
            month += 12
        y = year % 100
        c = floor(year/100)
        gamma = 5*c + floor(c/4)
        return (day+floor(26*(month+1)/10)+y+floor(y/4)+gamma+5) % 7 + 1

    def calc(self, start_year, end_year):
        cnt = 0
        for year in range(start_year, end_year+1):
            for month in range(1, 12+1):
                dow = self.get_day_of_week(year, month, 1)
                if dow == 7:
                    cnt += 1
        return cnt


class Loop:
    def get_days(self, year, month):
        if month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            return self.get_feb_days(year)
        else:
            return 31

    def get_feb_days(self, year):
        if year % 400 == 0:
            return 29
        elif year % 100 == 0:
            return 28
        elif year % 4 == 0:
            return 29
        else:
            return 28

    def calc(self):
        cnt = 0
        cum_days = 0
        for year in range(1900, 2000+1):
            for month in range(1, 12+1):
                days = self.get_days(year, month)
                # judge
                for day in range(1, days+1):
                    cum_days += 1
                    if cum_days % 7 == 0 and day == 1 and year > 1900:
                        cnt += 1
        return cnt


if __name__ == '__main__':
    print Loop().calc()
    print Zeller().calc(1901, 2000)
    print timeit.Timer('problem_019.Loop().calc()', 'import problem_019').timeit(10)
    print timeit.Timer('problem_019.Zeller().calc(1901, 2000)', 'import problem_019').timeit(10)
