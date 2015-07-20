# GetNetworks
# grabs list of current WiFi networks and dumps it back to Alfred feedback

import os, sys, WifiScan

'''
import os, sys, WifiScan, WifiScanYosemite
'''

from Feedback import Feedback

def run():
    
    # scan for available networks
    networks = WifiScan.find_access_points()
    
    '''
    networks = WifiScanYosemite.find_access_points()
    '''
    
    # Create the object to display networks
    feedback = Feedback()

    # Add the network items to feedback
    for mac in networks:
        feedback.add_item(networks[mac], mac, networks[mac], icon='OPEN.png')
        
    '''
    for TK in networks
        # how to specify the particular item below - e.g. the items and the record #??? 
        # e.g the SSID_STR from the 4th network?
        
        # encryption flag
        # CAPABILITIES key? an integer that contains info on encryption? 
        # look at scan data from airport utiliity for encrypted networks
        # how to pass it to here and what to do with it??
    
        feedback.add_item(networks[SSID_STR], networks[BSSID], icon=network_icon(networks[TK]))

        
     
     def get_network_icon(TK):
         if TK == 'NONE':
             return 'OPEN.png'
         else:
             return 'CLOSED.png'
    
    '''
    
    
    return feedback
        