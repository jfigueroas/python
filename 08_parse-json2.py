# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:51:32 2020

@author: CEC
"""

import urllib.parse
import requests

print("URL:" + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API status: " + str(json_status) + " = A successfull route call .\n" )