# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:27:59 2020

@author: CEC
"""

def reciproco(n):
    try: 
        n=1/n
    except ZerpDivisionError: 
        print("Division fallida")
        return None 
    else: 
        print("Todo salio bien")
    finally: 
        print("Es el momento de decir adios")
        return n
    
print(reciproco(1))