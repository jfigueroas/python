# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:24:57 2020

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
        return n
    
reciproco(1)

##########################################
