# adapted for use in WiFiPicker Alfred OSX by Anthony Townsend 18-July-2015
#
# OSX and Windows Wifi Scanner
# Created by Matt Silas
# https://github.com/MattSilas/Wifi-Scanner/blob/master/wifiscan.py

import sys
import plistlib
import urllib
import logging
import subprocess
import re

def find_access_points():
    """
    Parses the output from the airport utility into a single dictionary
    Airport's output is a plist; a list of dictionaries
    Keys can repeat for each plist node, so the values are appended into a list, to avoid overwriting
    Updated for OS X 10.10
    :return: dictionary with output from airport scan
    """
    from commands import getoutput
    scan = '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s -x'   
    root = getoutput(scan)
    output = plistlib.readPlistFromString(root)
    info = {}
    
    for node in output:
        temp_dict = parse_plist_output(node)

        for k, v in temp_dict.iteritems():
            if k in info:
                if isinstance(info[k], list):
                    info[k] = info[k] + [v]
                else:
                    info[k] = [info[k], v]
            else:
                info[k] = v
      
    return info

def parse_plist_output(node):
    """
    Parses a plist node, which can contain nested dictionaries
    The nested items are pulled out into a single k, v pair.
    If the same key is present in the dictionary, create a list of values
    :param node: dictionary
    :return: dictionary
    """
    return_val = {}
    try:
        for key, value in node.iteritems():
            if isinstance(value, dict):
                return_val.update(parse_plist_output(value))
            else:
                if key in return_val:
                    if isinstance(return_val[key], list):
                        return_val[key] = return_val[key] + [value]
                    else:
                        return_val[key] = [return_val[key], value]
                else:
                    return_val[key] = value
    except Exception as e:
        logging.exception("%s key: %s, value: %s", (e, key, value))
    
    return return_val


# TO DO make sure to sort by signal strength if possible

def parameters(signals):
    """
    Gets the RSSI and BSSID from the signals
    :param signals: dictionary from wifi scan
    :return: url encoded data request
    """
    data = {'BSSID': [], 'RSSI': []}
    keys = ['BSSID', 'RSSI']
    for key in keys:
        data[key].append(signals[key])

    return urllib.urlencode(data, True).replace("%3A", ":")



# MAKE JSON below here

if __name__ == "__main__":
    #print "Finding Access Points"
    
    if sys.platform == 'darwin':
        access_points = find_access_points()
    
    #   if sys.platform == 'linux2'or sys.platform == 'linux':
    #       print "no linux support currently"
    #       exit
    #   if sys.platform == 'win32':
    #       access_points = find_access_points_win()
        
    print "Encoding Parameters"
    params = parameters(access_points)
    url = "INSERT HERE"

# returns a JSON file at URL above? is this a useful output format, or should i pull the data after the fund_Access_points (e.g. cut everything below # MAKE JSON below here )
# might be useful to have the JSON just as a diagnostic

    f = urllib.urlopen(url %params)
    print "Retrieving JSON"
    print f.read()
