# WPA/WPA2 Theory

1. Theory
    1. Both WPA and WPA2 can be cracked using the same methods
        1. WPA is using TKIP enryption
        2. WPA2 is using CCMP enryption
    2. Much more secure than WEP

2. Feature - WPS: a feature that can be used with WPA & WPA2
    1. It slows devices to connect to the network easily without having to enter the key for the network
    2. It was designed to simplify the process of connecting printers and such devices.
    3. Can actually see a WPS button on most wireless enabled printers, if the button is pressed and then press the WPS button on the router, you'll notice that the printer will connect to the router without you having to enter the key.
    4. The Authentication is done using an 8 digit pin (only numbers)
        1. 8 digits is very small
        2. We can try all possible pins in relatively short time
        3. Then the WPS pin can be used to compute the actually password
    5. We're not exploting WPA or WPA2, we are acutally exploiting a feature that can be enabled on these encryptions
    6. This only works if the router is configured not to use PBC(Push Button Authentication)
    7. However, in most modern routers, PBC becomes enabled by default or WPS will be disabled by default so this method might not work. But it's always good to check whether it's enabled cuz WPA and WPA2 are so secured and so challenging.
