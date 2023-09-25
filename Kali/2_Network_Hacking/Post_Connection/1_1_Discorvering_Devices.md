# Discovering Devices Connected to the Same Network

1. Net Discover
    1. Since Virtual Machine can't get access to the local wireless adapter, thus, if want to attack a real PC or network wirelessly, we need a wireless adapter to connect to Kali and connect Kali to the network we want to attack to.
    2. In practice

```
# 1. 
netdiscover -r [Start IP]/24 
# -r: specify the IP range to search for
# If I type ifconfig, under the eth0(the virtual interface created by virtual box), for example inet 192.168.1.16, then the sub-net start at 192.168.1.0 to 192.168.1.254 as it's the last IP that a client can have
# Using /24 after it, the netdiscover will automatically know that I'm tyring to search for all of the IPS at the sub-net
```

2. Nmap
    1. Be able to see the open ports, running progrmas/services, computer name, operating system
    2. Bypass security/firewalls
    3. Zenmap is a graphical user interface of Nmap
    4. In practice

```
# 1. Connect to a wireless network

# 2. Open Zenmap
zenmap

# 3. Put the inet at the Target e.g. 182.168.1.1/24

# 4. Different among profile:
# 4.1 Ping Scan
```
