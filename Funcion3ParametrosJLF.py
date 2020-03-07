# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 18:47:14 2020

@author: CEC
"""

def address(street, city, postalCode):
    print("your address is:", street, "St.,", city, postalCode)
    
s= input("Street: ")
pC = input("Postal Code: ")
c = input ("City: ")

address(s,c,pC)