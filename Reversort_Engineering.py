#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 00:10:41 2021

@author: hienpham
"""
import os
import math
import sys



parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def find_array(list_, cost):
    flag = True
    sub_list = list_.copy()
    i = 0
    n_rev = 0
    while flag:
        first_zero_ind = list_.index(0)
        last_zero_ind = (len(list_) - 1) - list_[::-1].index(0)
        
        dist = last_zero_ind - first_zero_ind + 1
        if dist == 2 and cost == 1:
            list_[first_zero_ind] = i + 1 
            list_[last_zero_ind] = i + 2
            if n_rev%2 == 1:
                return list_.reverse()
            else:
                return list_
        elif dist == 2 and cost == 2:
            list_[first_zero_ind] = i + 2
            list_[last_zero_ind] = i + 1
            if n_rev%2 == 1:
                return list_.reverse()
            else:
                return list_
        else:
            if cost < 2*(dist - 1):
                cost -= 1
                list_[first_zero_ind] = i + 1
                
            else:
                cost -= dist
                list_[last_zero_ind] = i + 1
                list_.reverse()
                n_rev += 1
            
            i += 1
                
"""                
list_ = [0] * 35
cost = 581
list_new = find_array(list_, cost)
"""

def func(n, cost):
    if cost < (n - 1) or 2 * cost > (n - 1)*(n + 2):
        return 'IMPOSSIBLE'
    
    elif cost == (n - 1):
        array = ' '.join(str(x + 1) for x in range(n))
    
    else: 
        list_ = [0] * n
        find_array(list_, cost)
        array = ' '.join(str(x) for x in list_)
        
    return array

"""
import random

def gen_test(n_range, c_range):
    n = random.randint(2, n_range)
    c = random.randint(1, c_range)
    return n, c

def Reversort(L):
    cost = 0
    for i in range(len(L) - 1):
        j = L.index(min(L[i:len(L)]))
        L_sub = L[i:j+1]
        L_sub.reverse()
        cost += len(L_sub)
        L[i:j+1] = [element for element in L_sub]
    return L, cost

n, cost = gen_test(100, 1000)
array =  func(n, cost)
array_sorted, cost_sorted = Reversort(list(array.split(' ')))
#array = func(4, 6)

#L_sorted, cost = Reversort(L)
"""

def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n, cost = [int(i) for i in parse_input().split()]
        result = func(n, cost)
        print("Case #{}: {}".format(i+1, result))
        
if __name__ == "__main__":
    main()
