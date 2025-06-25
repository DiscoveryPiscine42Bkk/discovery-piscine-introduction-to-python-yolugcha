#!/usr/bin/env python3

import sys
if len(sys.argv) == 2: 
    first = sys.argv[1]
    check = input("What was the parameter? ")
    if first == check:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")