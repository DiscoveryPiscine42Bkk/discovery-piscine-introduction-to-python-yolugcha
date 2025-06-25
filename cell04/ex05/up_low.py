#!/usr/bin/env python3

text = input()
for char in text:
    if char.isupper():
        char = char.lower()
    else:
        char = char.upper()
    print(char, end = "")
print ()