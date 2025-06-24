#!/usr/bin/env python3

import sys

if len(sys.argv) > 1: 
    print("none")
else:
    n = 0
    while n <= 10:
        num = 0
        print(f"Table de {n}: ", end="")
        while num <= 10:
            print(f"{n*num}", end = " ")
            if num == 10:
                print(end = "\n")
            num += 1
        n += 1
