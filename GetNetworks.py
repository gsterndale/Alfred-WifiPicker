# GetNetworks
# grabs list of current WiFi networks and dumps it back to Alfred feedback

# TO DO ADD BACK when figure out to set an encryption flag properly

#   def get_network_icon(encryption):
#       if encryption == 'NONE':
#           return 'OPEN.png'
#       else:
#           return 'CLOSED.png'

# TO DO why can't we just transpose from the dictionary created by WifiScan to the Feedback function call?


import os, WifiScan
from Feedback import Feedback

def run():
    
    networks = WifiScan.find_access_points()
    network_list = []
    
    for ssid in networks:
        network_list.append((ssid))
        # TO DO replace above line with network_list.append((ssid. macaddr, '', icon = network_icon))

    # Create the object to display networks
    feedback = Feedback()

    # Add the network items to feedback
    
    for ssid in network_list:
        
        # replace icon with network_icon later (see subroutine at bototm)
        feedback.add_item(ssid, ssid, '', icon='OPEN.png')
        
    return feedback
        