#OSX and Windows Wifi Scanner
#Created by Matt Silas
#https://github.com/MattSilas/Wifi-Scanner/blob/master/wifiscan.py
#Modified by Anthony Townsend 14 July 2015

import sys
import xml.etree.ElementTree as ET

# debug
print "This is WifiScan.py's contents"
    

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
        address = access_point.find("string").text
        
        # 2nd string is SSID
        # THIS SEEMS TO BE FAILING
        ssid = access_point.findall("string")[1].text
        
        # 8th integer is signal strength
        # is this sorting by signal strength?s
        strength = abs(int(access_point.findall("integer")[7].text))
        access_points[address] = strength
        
        # is there some missing append thing not happening?
        # e.g. from MOUNTED --> volume_tuples.append((volume_name, subtitle, volume_arg, volume_icon))
        # but this came back as a dictionary, so... how to do it? extract first from dictionary into a tuple?
        # access_points.append(ssid, address, strength)
        
        # TO DO figure out a way to grab encryption either YES or NONE set a flag
        
        # DEBUG print counter
        d += 1
        print d, ssid, address, strength
        
    return access_points