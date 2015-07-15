# Script to Debug Various Aspects of Workflow

import os, WifiScan

def run():
    # returns a dictionary list of networks as ssids and macs sorted by signal strength
    networks = WifiScan.find_access_points()
    
    # debug
    print "This is Debug.py's contents"
    
    # theres something wrong with the rest of this... per sample output below
    # but the data does seem to be coming back from WifiScan
    # so Debug.py's job is done for now 15-July-2015 6:22pm EDT
    
    '''
    This is WifiScan.py's contents
    GBC-Guests f0:b0:52:9:e7:38 88
    Test-Guests f0:b0:52:9:e3:dc 91
    Test-Guests e0:10:7f:17:ba:2c 77
    GBC-Guests f0:b0:52:9:e6:f8 85
    GBC-Guests f0:b0:52:9:e9:d8 91
    GBC-Guests 0:16:4:0:51:28 48
    Test-Guests e0:10:7f:57:ba:28 65
    GBC-Guests e0:10:7f:17:ba:28 65
    GBC-GUESTS 0:16:4:0:1b:46 75
    This is Debug.py's contents
    SSID e0:10:7f:17:ba:2c
    Traceback (most recent call last):
      File "Debug.py", line 27, in <module>
        print run()
      File "Debug.py", line 14, in run
        print "Address %s" % macaddr
    NameError: global name 'macaddr' is not defined
    '''
    
    for ssid in networks:
        print "SSID %s" % ssid
        print "Address %s" % macaddr
        print "Strength %s" % strength
        
print run()