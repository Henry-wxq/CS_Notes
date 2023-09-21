# Basics

## Typical Network
1. A client can only get access to the resources, e.g. internet, throught an access point which for example a router. None of the clients, i.e. the computers, connected to the network can access the resource without the access point, i.e. the router.

## Connect a USB adapter to Kali(Wireless Adapter as an example)
1. Wireless Adapter is used for Wi-Fi cracking.
      1. Built-in Wireless Cards:
            1. Can't be used in virtual machines
            2. Not good enought for hacking
      2. Requirements
            1. Monitor Mode
            2. Packet Injection
            3. AP mode
      3. Selecting
            1. Wireless Chipset('Brains', 'Capability')
                  1. Atheros AR9271(Good except no 5Ghz Support)(e.g. Alfa AWUS036NHA)
                  2. Realtek RTL8812AU(Good except difficult installation(e.g. Alfa AWUS036ACH))
2. Setting
      1. Before plug in the Wireless Adapter: Vmware - Right Click the Kali Machine - Settings - Add - USB Controller - USB compatibility: USB 3.1; Show all USB input devices - OK
      2. Start Kali - Terminal - ifconfig
            1. eth0: virtual ethernet interface, created by VMware for the cirtual machine through the virtual NOC network
            2. lo: virtual interface, cirtual loopback interface used in Linux
      3. Plug in the Wireless Adapter -  Connect to virtual Machine
      4. igconfig
            1. wlan0(exists then connection is done): wireless adapter just connected to Kali
