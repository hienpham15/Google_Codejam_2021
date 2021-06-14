#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 19:13:23 2021

@author: hienpham
"""

import os
import math
import sys



parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def Reversort(L):
    cost = 0
    for i in range(len(L) - 1):
        j = L.index(min(L[i:len(L)]))
        L_sub = L[i:j+1]
        L_sub.reverse()
        cost += len(L_sub)
        L[i:j+1] = [element for element in L_sub]
    return L, cost


def func(L, n):
    L_sorted, cost = Reversort(L) 
    return cost


#L = [2, 4, 3, 1]
#L_sorted, cost = Reversort(L)

def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n = int(parse_input())
        L = parse_input()
        L = list(L.split(" "))
        L = [int(i) for i in L]
        result = func(L, n)
        print("Case #{}: {}".format(i+1, result))
        
if __name__ == "__main__":
    main()
