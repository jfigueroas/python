# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 20:16:37 2020

@author: CEC
"""

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
    print("Directions from " + (orig) + " to " + (dest))
    print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
    print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
    print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
    print("=============================================")
    print("=============================================")
    for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
    print("=============================================\n")