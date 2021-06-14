#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 17:53:47 2021

@author: hienpham
"""

import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def median_sort(N):
    
    median = []
    for i in range(N//2 - 2):
        print("{} {} {}".format(i, i + 1, i + 2))
        median.append(int(parse_input()))
    order = [0] * 5
    order
    
    return 


def func(L, n):
    #L_sorted, cost = Reversort(L) 
    return 




def main():
    n_cases, N, Q = [int(i) for i in parse_input().split()]
    for i in range(n_cases):
        median_sort(N)
        result = func()
        print("Case #{}: {}".format(i+1, result))
        
if __name__ == "__main__":
    main()