# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 11:27:53 2020

@author: CEC
"""

import numpy as np
import sys 
print ("USO DE MEMORIA PYTHON")
S= range(1000)
print(sys.getsizeof(S)*len(S))
print("\n"*1)
print("USO DE MEMORIA NUMPY")
D= np.arange(1000)
print()