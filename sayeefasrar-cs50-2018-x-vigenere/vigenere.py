import sys
from cs50 import get_string

if len(sys.argv) != 2:
    print("Command line arguement error!")
    exit(1)

#length_of_argv[1] = len(sys.argv[1])
keyascii = []
#i = 0

for c in (sys.argv[1]):
    if c.isalpha() and c.isupper():
        keyascii.append(ord(c) - 65)
    elif c.isalpha() and c.islower():
        keyascii.append(ord(c) - 97)
    else:
        print("Command line argument eror!")
        exit(1)
    #i += 1

#print("plaintext: ", end = "")
s = get_string("plaintext: ")
print("ciphertext: ", end="")

j = 0
for c1 in s:
    k = j % len(sys.argv[1])
    if c1.isalpha() and c1.isupper():
        alphabet = (ord(c1) - 65 + keyascii[k]) % 26
        ASCII = 65 + alphabet
        print(chr(ASCII), end="")
    elif c1.isalpha() and c1.islower():
        alphabet = (ord(c1) - 97 + keyascii[k]) % 26
        ASCII = 97 + alphabet
        print(chr(ASCII), end="")
    else:
        print(c1, end="")
    j += 1

print()