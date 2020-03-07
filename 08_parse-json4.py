# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 20:04:27 2020

@author: CEC
"""

import urllib.parse
import requests

while True: 
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q": 
        break
    dest = input("Destination: ")
    if dest == "quit" or orig == "q": 
        break
    url = main_api+urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print("URL: " + (url))
