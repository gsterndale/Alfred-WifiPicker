# GetNetworks
# grabs list of current WiFi networks and dumps it back to Alfred feedbak

import os, WifiScan
from Feedback import Feedback

# networks is just a list for now, make it a tuple later to add other fields?

def run():
    networks = WifiScan.find_access_points_osx()
    
    # debugging - print the list of ssids to check if data coming back from WiFiScan
    #for ssid in networks:
    #    print ssid
    
    
    # Append Values to tuple - later on when more than one field coming back from WiFiScan, see the Mounted.py example
    # for ssid in networks:
        #
        #  networks_tuple.append((ssid))


    # Create the object to display networks
    feedback = Feedback()

    # Add the network items
    # DEBUG check maybe its been barfing because i dont have enough fields in Feedback?
    # EXAMPLE from Mounted.py:
    # feedback.add_item(volume_name, subtitle, volume_arg, icon=volume_icon)
    
    # DEBUG is it barfing because it doesnt know what 'ssid' fields means in networks because it came from the function call? 
    for ssid in networks:
        
        feedback.add_item(ssid, "A network to pick...", "", icon="OPEN.png")

    return feedback
        

# TO DO
# add back if - else loop to get the icon
#
# def get_network_icon(encryption):
#    if encryption == 'NONE':
#        return 'OPEN.png'
#    else:
#    return 'CLOSED.png'

