#!/usr/bin/env python3

num = float(input("Give me a number: "))
if num.is_integer():
    print (int(num))
else:
    print (int(num+1))