# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:15:32 2020

@author: CEC
"""
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Quito"
dest = "Ibarra"
key = "gCClR6htV0likj9nbl5ZPpBvv73LKs2v"

url = main_api+urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data)