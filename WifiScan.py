#OSX and Windows Wifi Scanner
#Created by Matt Silas
#https://github.com/MattSilas/Wifi-Scanner/blob/master/wifiscan.py
#Modified by Anthony Townsend 14 July 2015

import sys
import xml.etree.ElementTree as ET

#Runs OSX Airport utility with scan and xml out flags set
def find_access_points():
    
    from commands import getoutput
    
    scan = '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s -x'   
    root = ET.fromstring(getoutput(scan))
    output = root.getchildren()[0]
    access_points = {}
    d = 0

    for access_point in output:
        
        # 1st string is MAC address
        macaddr = access_point.find("string").text
        print >> sys.stderr, macaddr
                
        # 2nd string is SSID
        # DEBUG this -is- working but its the MAC not the SSID
        # DEBUG is this because the first string is the country code (e.g. 'US'?)
        ssid = access_point.findall("string")[1].text
        print >> sys.stderr, ssid  
        
        # 8th integer is signal strength
        strength = abs(int(access_point.findall("integer")[7].text))
        print >> sys.stderr, strength
        
        # is this sorting by signal strength?
        access_points[macaddr] = strength
        
        
        # TO DO figure out a way to grab encryption either YES or NONE set a flag
        
    return access_points