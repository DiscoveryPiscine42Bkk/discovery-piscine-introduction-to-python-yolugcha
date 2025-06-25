#!/usr/bin/env python3

import sys
import re

if len(sys.argv) < 2: 
    print("none")
else:
    x = sys.argv[1]
    y = sys.argv[2]

    found = re.findall(rf"{x}", y)

    print(len(found))