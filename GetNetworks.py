# GetNetworks
# grabs list of current WiFi networks and dumps it back to Alfred feedbak

import os, WifiScan
from Feedback import Feedback

network_tuples = []

def run():
    networks = WifiScan.find_access_points_osx()
    
    for address in networks:
        
        # Append Values to tuple
        # DEBUG - NEED TO TEST
        # is this actually passing any data into network_tuples?
        #
        network_tuples.append((ssid, address))
        

    # Create the object to display networks
    feedback = Feedback()

    # Add the network items

    for ssid in network_tuples:
        
        feedback.add_item(ssid, address)

    return feedback
        
"""

# Get Encryption Status STARTER
      encryption = re.search('Protocol:\s+(.+)', extra_info)
      if volume_prot:
         volume_prot = volume_prot.group(1)
         volume_icon = get_volume_icon(volume_prot)
         if volume_prot == 'SATA':
            continue
      else:
         continue


# TO FIX
# add back if - else loop when figure out how to grab encryption info
#
# def get_network_icon(encryption):
#    if encryption == 'NONE':
#        return 'OPEN.png'
#    else:
#    return 'CLOSED.png'

	  
"""
