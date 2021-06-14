#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 21:13:48 2021

@author: hienpham
"""

import os
import math
import sys



parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def window(sub_mural):
    if sub_mural[2] != '?':
        sub_mural[1] = sub_mural[0]
    else:
        sub_mural[1] = sub_mural[0]
        sub_mural[2] = sub_mural[0]
    return sub_mural

def func(costX, costY, mural):
    total_cost = 0
    i = 0
    
    if not mural:
        return 0
    
    while i <= len(mural) - 1:
        if mural[i] != '?':
            i += 1
        else:
            if i != 0:
                if i != len(mural) - 1:
                    sub_mural = mural[i-1:i+2]
                    new_mural = window(sub_mural)
                    mural[i-1:i+2] = [element for element in new_mural]
                    i += 2
                else:
                    mural[i] = mural[i-1]
            else:
                if 'C' in mural and 'J' not in mural:
                    first_C_ind = mural.index('C')
                    mural[0:first_C_ind] = ['C' for _ in range(first_C_ind)]
                    i += first_C_ind
                elif 'J' in mural and 'C' not in mural:
                    first_J_ind = mural.index('J')
                    mural[0:first_J_ind] = ['J' for _ in range(first_J_ind)]
                    i += first_J_ind
                elif 'C' in mural and 'J' in mural:
                    first_C_ind = mural.index('C')
                    first_J_ind = mural.index('J')
                    if first_C_ind < first_J_ind:
                        mural[0:first_C_ind] = ['C' for _ in range(first_C_ind)]
                        i += first_C_ind
                    else:
                        mural[0:first_J_ind] = ['J' for _ in range(first_J_ind)]
                        i += first_J_ind
                else:
                    return 0
                
    for j in range(len(mural) - 1):
        if mural[j] == 'C' and mural[j+1] == 'J':
            total_cost += costX
        elif mural[j] == 'J' and mural[j+1] == 'C':
            total_cost += costY
    
    return total_cost


#import random
#import string
 

#def gen_test(x_range, y_range, allowed_chars, s_range):
#    costX = random.randint(1, x_range)
#    costY = random.randint(1, y_range)
#    str_size = random.randint(1, s_range)
#    mural = ''.join(random.choice(allowed_chars) for x in range(str_size))
#    return costX, costY, mural

#costX, costY, mural = gen_test(100, 100, 'CJ?', 10)
#costX = 64
#costY = 55
#mural = '?JC???J?'
#cost = func(costX, costY, list(mural))


def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        costX, costY, mural = parse_input().split()
        result = func(int(costX), int(costY), list(mural))
        print("Case #{}: {}".format(i+1, result))
        
if __name__ == "__main__":
    main()
