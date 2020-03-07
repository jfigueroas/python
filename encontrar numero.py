# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 19:54:25 2020

@author: CEC
"""

def validarNumero(prompt, min, max): 
    while (True): 
        try: 
            x=int(input(prompt))
            assert x>= min and x <= max
            return x
            break
        except ValueError: 
            print("Ingresar solo numeros")
        except: 
            print("El valor debe estar dentro del rango")
            
v = validarNumero("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
