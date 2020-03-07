# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 12:22:00 2020

@author: CEC
"""

import pandas as pd 
titulos = pd.read_csv('data/titles.csv')
print(titulos.head(100))
print("\n"*2)
elenco=pd.read_csv(data/cast.csv, encoding='utf-8')
print(elenco.head(10))