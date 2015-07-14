#OSX and Windows Wifi Scanner
#Created by Matt Silas
#Modified by Anthony Townsend 14 July 2015

import sys
import xml.etree.ElementTree as ET

#Runs OSX Airport utility with scan and xml out flags set
def find_access_points_osx():
    from commands import getoutput
    scan = '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s -x'   
    root = ET.fromstring(getoutput(scan))
    output = root.getchildren()[0]

    access_points = {}

    for access_point in output:
        # 1st string is MAC address
        address = access_point.find("string").text
        # 2nd string is SSID
        ssid = access_point.findall("string")[1].text
        # 8th integer is signal strength
        # strength = abs(int(access_point.findall("integer")[7].text))
        # access_points[address] = strength

    return access_points