# Wordlisst

1. Handshake Packets
    1. The handshake doesn't contain data that helps recover the key
    2. It contains data that can be used to check if a key is falue or not
    3. Therefore, what we're going to do is to create a wordlist which is basically a big text file that contains a large number of passwords.
    4. Then go through this file, go through the passwords one by one, and use them with the handshake in order to check whether this password is valid or not.

2. Create your own wordlist: using crunch(VERY IMPORTANT!)(Will be used in penetration)
    ```
    # 1. Create the wordlist
    crunch [min] [max] [characters]  -o [filename] (-t [pattern])

    # min: the minimum number to generate(can check by the phone when the target network shows can be joined which is the min)
    # max: the maximum number to generate
    # characters: the characters that you wnat to generate passwords from
    # -t: optional, to give a pattern of the password
    # -o: the file name that the passwords are gonna be stored.
    # e.g. crunch 6 8 123abc$ -o wordlist -t a@@@@b
    # can use: man crunch to check more advanced usage of crunch

    # 2. open the file(Ctrl + C out of it)
    cat [filename]
    ```
