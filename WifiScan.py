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
    
    print >> sys.stderr, "This is WifiScan.py"

    for access_point in output:
        
        
        # TO DO filter out multiple APs for the same SSID (probably flip the key:value scheme) 
    
        # 1st string is MAC address - the dictionary's key
        mac = access_point.find("string").text
                
        # 2nd string is SSID
        ssid = access_point.findall("string")[1].text
        
        # TO DO figure outa way to pass out these two variables back
        # TO DO how did the original script do it?

        # encryption either YES or NONE set a flag

        # 8th integer is signal strength
        # strength = abs(int(access_point.findall("integer")[7].text))

        # set the value portion of dictionary's {key:value} pair!!!
        access_points[mac] = ssid
        
    return access_points