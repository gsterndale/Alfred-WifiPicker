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
    
    # networks is a dictionary that contains list of MAC:SSID pairs
    # but its coming back empty -- hence the {}

    networks = WifiScan.find_access_points()

    print >> sys.stderr, "This is GetNetworks.py"
    print >> sys.stderr, networks
    

    # Create the object to display networks
    feedback = Feedback()

    # Add the network items to feedback
    
    for ssid in networks:
        
        # replace icon with network_icon later (see subroutine at bototm)
        feedback.add_item(ssid, '', '', icon='OPEN.png')
        
    return feedback
        