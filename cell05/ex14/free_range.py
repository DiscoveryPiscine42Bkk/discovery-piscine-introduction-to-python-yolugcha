#!/usr/bin/env python3

import sys 
if len(sys.argv) < 2:
    print("none")
else:  
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    arr = []
    while num1 <= num2:
        arr.append(num1)
        num1 += 1
    print (arr)