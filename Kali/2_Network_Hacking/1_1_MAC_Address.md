# MAC Address
1. MAC(Media Access Control)
    1. Properties:
        1. Permanent
        2. Physical
        3. Unique
        4. Assigned by Manufacturer(No two same MAC Address devices)(If we unplug and connect to another PC, the MAC Adress will still be the same)
    2. The MAC Address is used within the networkto identify devices and transfer data between devices.
    3. Each package contains a source MAC and a destination MAC. So it will flow though

2. Change MAC Address
    1. Why?
        1. Increase anonymity
        2. Impersonate other devices
        3. Bypass filters
    2. How to change
        1. List out all the network interface(any device that allow us to connect to a network): in Terminal:

        ```
        ifconfig
        # eth0 is show the network kai is connecting to which is actually a virtual NAT network
        # ether is show the MAC address of this virtual interface
        # e.g. 08:00:27:59:1b:51
        ```

        2. Firstly disable an interface
        ```
        ifconfig [interface name] down
        ```

        3. Change the option we want to change
        ```
        ifconfig [interface name] hw ether [MAC wants to change]
        # hw: Hardware Address
        # example MAC(Make sure it starts from 00): 00:11:22:33:44:55
        ```

        4. Enable the interface
        ```
        ifconfig [interface] up
        ```
    3. Reminder: the MAC Adress will change back to the original one once restart the computer.


