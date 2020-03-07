# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 11:22:54 2020

@author: CEC
"""

import numpy as np#convension de buenas practicas 

a=np.array([1,2,3])
print(a)

b=np.array([(1,2,3),(4,5,6),(7,8,9)])
print(b) 

###############

unos = np.ones((3,4))
print(unos)

#################

# crear una matriz con valores aleatorios

aleatorios=np.random.random((2,2))
print(aleatorios)

##############
# matriz vacia 

vacia=np.empty((3,2))
print(vacia)


######################
#matriz de un solo valor 
full=np.full((1000,100),12)
print(full)

####################
#crear una matriz con valores espaciados uniformemente
espacio1=np.arange(0,30+1,5)
print(espacio1)


espacio2= np.linspace(0,2,5)
print(espacio2)

############
#matriz I 

identidad1= np.eye(4,4)
print(identidad1)

identidad2=np.identity(5)
print(identidad2)

#######
#dimensiones de una matriz

a=np.array([(1,2,3),(4,5,6)])
#d=a.dim


##############
#cambio de forma de una matriz 
a=np.array([(8,9,10),(11,12,13)])
print(a)
print("\n"*2)
#a=a


#################
#encontrar un numero dentro de una matriz 
a=np.array([(1,2,3,4),(3,4,5,6)])
print(a)
print("\n"*1)
print(a[1,2])

#################
#encontrar un numero dentro de una matriz 
a=np.array([(1,2,3,4),(3,4,5,6)])
print(a)
#print("\n"*1)
print(a[0:,1])



#################
#encontrar la raiz cuadrada y de dev estandar de la matriz
a=np.array([(1,2,3,4),(3,4,5,6)])
print("\n"*1)
print(a[0:,1])
print(np.sqrt(a))
print("\n"*2)
print(np.std(a))

##################
#operaciones con matrices 
a=np.array([(1,2,3,4),(3,4,5,6)])
b=np.array([(1,2,3,4),(3,4,5,6)])

print(a+b)
print("\n")
print(a-b)
print("\n")
print(a*b)
print("\n")
print(a/b)








