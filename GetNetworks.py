# GetNetworks
# grabs list of current WiFi networks and dumps it back to Alfred feedbak

import os, WifiScan
from Feedback import Feedback

# networks is just a list for now, make it a tuple later to add other fields?

def run():
    networks = WifiScan.find_access_points()
    
    # Get additional data and append it to tuple
    
    network_tuples = []
    
    for ssid in networks:
        # replace icon with network_icon later (see subroutine at bototm)
        network_tuples.append((ssid, mac))
        

    # Create the object to display networks
    feedback = Feedback()

    # Add the network items
    # DEBUG check maybe its been barfing because i dont have enough fields in Feedback?
    # EXAMPLE from Mounted.py:
    # feedback.add_item(volume_name, subtitle, volume_arg, icon=volume_icon)
    
    # DEBUG is it barfing because it doesnt know what 'ssid' fields means in networks because it came from the function call? 
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

