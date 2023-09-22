# WEP Theory

1. WEP(Wired Equivalent Privacy): Old Encryption
    1. Algorithm: RC4
        1. Client encrypts data using a key
            1. Each packet sent into the air WEP tries to create an unique key.
            2. WEP generates a random 24 bit initialization vector
            3. The initialization vector(IV) is then added to the password of the network to the actual key that people use to connect to the network
            4. This generates a Key stream which is used to encrypt this packet and transform it into gibberish
            5. IV + Key(password) = Key stream
        2. Encrypted packet sent in the air
            1. Since the router already has the Key, the packet contains the IV
        3. Router decrypts packet using the key
    2. Weakness
        1. Anyone capture the packet will be able to see the IV in plain text
        2. The size of IV is only 24 bit. The IV will start getting repeated in a buzy network. This makes WEP vulnerable to statistical attacks
        3. We can use a toll called airtrack-ng to determine the ket stream, once we have enough repeated IVs, then it will also be able to crack WEP and give us the key to the network


