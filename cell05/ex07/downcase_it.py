#!/usr/bin/env python3

import sys
if len(sys.argv) <= 1: 
    print("none")
else:
    lowercase_text = sys.argv[1].lower()
    print(lowercase_text)
