# GetNetworks
# grabs list of current WiFi networks and dumps it back to Alfred feedbak

import os, WifiScan
from Feedback import Feedback


def run():
    networks = WifiScan.find_access_points_osx()
    network_tuples = []
    
    for address in networks:
        
        # Append Values to tuple
        # DEBUG
        # this isnt throwing any errors but not passing any data either now
        #
        mac = address
        netname = ssid
        network_tuples.append((netname, mac))
        

    # Create the object to display mounts
    feedback = Feedback()

    # Add the network items
    for mac in network_tuples:
        
        # feedback.add_item(volume_name)
        feedback.add_item(netname, mac)

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

# 

# TO FIX
# add back if - else loop when figure out how to grab encryption info
#
# def get_network_icon(encryption):
#    if encryption == 'NONE':
#        return 'OPEN.png'
#    else:
#    return 'CLOSED.png'

	  
"""
