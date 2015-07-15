# Script to Debug Various Aspects of Workflow

import os, WifiScan


# Test WiFiScan data return

def run():
    # returns a dictionary list of networks as ssids and macs sorted by signal strength
    networks = WifiScan.find_access_points()
    
    # print the whole dictionary
    
    for ssid in networks:
        print "SSID " ssid
        print "MAC " mac
        print "signal " signal
        
        
        # Sample code for printing a nested dictionary
        # for x in cars:
        #    print (x)
        #    for y in cars[x]:
        #        print (y,':',cars[x][y])
        
        