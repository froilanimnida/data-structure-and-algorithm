"""
# Caesar cipher.
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)

# Reverse of the Caesar cipher.
# Caesar cipher - decrypting a message.
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)
"""
"""Assuming that the key is 1, we can write a function that encrypts and decrypts a message.
You are already familiar with the Caesar cipher, and this is why we want you to improve the code we showed you
recently.
The original Caesar cipher shifts each character by one: a becomes b, z becomes a, and so on. Let's make it a bit
harder, and allow the shifted value to come from the range 1..25 inclusive.

Moreover, let the code preserve the letters' case (lower-case letters will remain lower-case) and all non-alphabetical
characters should remain untouched.

Your task is to write a program which:
asks the user for one line of text to encrypt;
asks the user for a shift value (an integer number from the range 1..25 - note: you should force the user to enter a
valid shift value (don't give up and don't let bad data fool you!)
prints out the encoded text.
Test your code using the data we've provided.

Sample input:
abcxyzABCxyz 123
2

Sample output:
cdezabCDEzab 123

Sample input:
The die is cast
25
Sample output:
Sgd chd hr bzrs
"""


def caesar_cipher(message, shift_count):
    result = ""
    lower_limit = [97, 122]
    upper_limit = [65, 90]
    for ch in message:
        if ch.isspace():
            result += " "
        elif ch.islower():
            if ord(ch) + shift_count > 122:
                i = (ord(ch) + shift_count) - 122
                result += chr(96 + i)
            else:
                result += chr(ord(ch) + shift_count)
        elif ch.isupper():
            if ord(ch) + shift_count > 90:
                i = (ord(ch) + shift_count) - 90
                result += chr(64 + i)
            else:
                result += chr(ord(ch) + shift_count)
        else:
            result += ch
    return result


try:
    x = input("Enter your message: ")
    y = int(input("Shift count: "))
    print(caesar_cipher(x, y))
except ValueError:
    print("You entered wrong value.")


