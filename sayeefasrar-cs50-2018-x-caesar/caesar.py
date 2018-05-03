import sys
from cs50 import get_string

if len(sys.argv) == 2:
    key = int(sys.argv[1])
else:
    print("Command line arguement error!")
    exit(1)


s = get_string("Plaintext: ")
print("ciphertext: ", end="")

for c in s:
    if c.isalpha() and c.isupper():
        alphabet = (ord(c) - 65 + key) % 26
        ASCII = chr(65 + alphabet)
        print(f"{ASCII}", end="")
    elif c.isalpha() and c.islower():
        alphabet = (ord(c) - 97 + key) % 26
        ASCII = chr(97 + alphabet)
        print(f"{ASCII}", end="")
    else:
        print(f"{c}", end="")
print()