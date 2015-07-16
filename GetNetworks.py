# GetNetworks
# grabs list of current WiFi networks and dumps it back to Alfred feedback

# TO DO ADD BACK when figure out to set an encryption flag properly

#   def get_network_icon(encryption):
#       if encryption == 'NONE':
#           return 'OPEN.png'
#       else:
#           return 'CLOSED.png'


import os, WifiScan
from Feedback import Feedback

def run():
    
    networks = WifiScan.find_access_points()
    network_list = []
    
    
    
#
# TO DO something is happening that ssid is getting interpreted improperly below, perhaps it has to do with the ordering?
# TO DO do i have to tell this script to assign whats coming back to variables by order? 
# TO DO seems like its taking the first piece of data back (which is the mac) and assigning it to the ssid in the section below
#

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
        