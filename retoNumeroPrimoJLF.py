# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 19:18:51 2020

@author: CEC
"""

def isPrime (num):
    if num < 1: 
        return False
    elif num == 2:
        return True
    else: 
        for i in range(2, num): 
            if num % i == 0:
                return False 
            return True 
    #   






for i in range (1,20):
    if isPrime(i + 1):
        print(i+1, end = " ")
        
print()