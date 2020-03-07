# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:36:19 2020

@author: CEC
"""

def readint(prompt, min, max):
    v = int(input(prompt))
    
    if v > max or v < min:
        raise Exception("El numero no esta en el rango. Intente nuevamente")
        
    try: 
        return v
    except ZeroDivisionError: 
        print("Ingrese un numero válido. Intente nuevamente: ")
        
         
   
  
v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
