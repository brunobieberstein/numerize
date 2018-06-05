#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 13:49:15 2018

@author: Bruno
"""

from decimal import Decimal

len_destinator = {1 : 1, 2 : 1, 3 : 1, 4 : 1000, 5 : 1000, 6 : 1000, 7 : 1000000, 8 : 1000000, 9 : 1000000, 10 : 1000000000,11 : 1000000000, 12 : 1000000000, 13 : 1000000000000,14 : 1000000000000, 15 : 1000000000000}
KMBT = {1 : '', 2 : '', 3 : '', 4 : 'K', 5 : 'K', 6 : 'K', 7 : 'M', 8 : 'M', 9 : 'M', 10 : 'B', 11 : 'B', 12 : 'B', 13 : 'T',14 : 'T', 15 : 'T'}


def round_num(n, decimals):
    return n.to_integral() if n == n.to_integral() else round(n.normalize(), decimals)

def drop_zero(n):
    n = str(n)
    return n.rstrip('0').rstrip('.') if '.' in n else n

def numerize(n, decimals=2):
    n_neg = int(n)
    n_int = abs(Decimal(n))
    is_negative_string = ""
    if n_neg < 0:
        is_negative_string = "-"
    if len(str(n_int)) <= 15:
        return is_negative_string + str(drop_zero(round_num(n_int / len_destinator[len(str(n_int))], decimals))) + KMBT[len(str(n_int))]
    else:
        return is_negative_string + str(n_int)

if __name__ == '__main__':
    n = input('Zahl: ')
    decimals = input('Decimals: ')
    print(numerize(n, decimals))
