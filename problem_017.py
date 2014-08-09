#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
If the numbers 1 to 5 are written out in words:
one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were
written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
'''

import timeit

a01_09 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
a10_19 = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
          'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
a2X_9X = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


len01_09 = len(''.join(a01_09))
len10_19 = len(''.join(a10_19))
len2X_9X = len(''.join(a2X_9X))

def thousand():
    return hundred()*10 + \
           (len01_09*100 + len('hundred')*900 + len('and')*(900-9)) + \
           len(''.join(['one', 'thousand']))

def hundred():
    return len01_09 + len10_19 + (len2X_9X*10 + len01_09*len(a2X_9X))

if __name__ == '__main__':
    print thousand()
    print timeit.Timer('problem_017.thousand()', 'import problem_017').timeit(10)
