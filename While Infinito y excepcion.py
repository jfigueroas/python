# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 19:21:50 2020

@author: CEC
"""

from time import sleep 
seconds=0
while True: 
    try: 
        print(seconds)
        seconds+=1
        sleep(1)
    except KeyboardInterrupt:
        break
        #print("No hagas eso")