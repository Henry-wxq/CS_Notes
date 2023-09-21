# Wireless Modes
1. Aim: Since the packages are send in the air, we are able to capture the package although we don't have the destination MAC.
2. Change the wireless interface in the monitor mode:
    1. Check the current mode
    ```
    iwconfig
    # To see the wireless interfaces only
    # Show: Mode: Managed (which means it will only capture package has the same destination MAC address as the device MAC address)
    ```
    2. Disable the interface

    3. Run a command to kill any process that could interfere with using my interface

    ```
    airmon-ng check kill
    # kill the wireless manager
    ```

    4. Enable the monitor mode
    ```
    iwconfig [interface name] mode monitor
    ```

    5. Enable the interface
    6. Check the mode
