# GetNetworks
# grabs list of current WiFi networks and dumps it back to Alfred feedbak

import os, WifiScan
from Feedback import Feedback

def run():
    
    # returns a dictionary list of networks as ssids and macs sorted by signal strength
    networks = WifiScan.find_access_points()
    
    # Get additional data and append it to tuple
    
    network_tuples = []
    
    for ssid in networks:
        # replace icon with network_icon later (see subroutine at bototm)
        network_tuples.append((ssid, mac))
        

    # Create the object to display networks
    feedback = Feedback()

    # Add the network items
    
    #
    # DEBUG -- print contents of network_tuples at this point
    # print "lala %r" % thisthing -- Use the %r for debugging, since it displays the "raw" data of the variable
    # ???print network_tuples[]
    
    # DEBUG potential other option of using the new workflow.py code for creating the Feedback instead
    
    for ssid in network_tuples:
        
        # replace icon with network_icon later (see subroutine at bototm)
        feedback.add_item(ssid, mac, '', icon='OPEN.png')
        
    return feedback
        

# TO DO ADD BACK when figure out encryption flag
#
# def get_network_icon(encryption):
#    if encryption == 'NONE':
#        return 'OPEN.png'
#    else:
#    return 'CLOSED.png'

