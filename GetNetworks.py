# GetNetworks
# grabs list of current WiFi networks and dumps it back to Alfred feedback

# TO DO ADD BACK when figure out to set an encryption flag properly
#   def get_network_icon(encryption):
#       if encryption == 'NONE':
#           return 'OPEN.png'
#       else:
#           return 'CLOSED.png'

import os, sys, WifiScan
from Feedback import Feedback
def run():
    
    # scan for available networks
    networks = WifiScan.find_access_points()

    # Create the object to display networks
    feedback = Feedback()

    # Add the network items to feedback
    for mac in networks:
        
        # replace icon with network_icon later (see subroutine at bototm)
        feedback.add_item(networks[mac], mac, networks[mac], icon='OPEN.png')
        
    return feedback
        