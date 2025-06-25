#!/usr/bin/env python3

import sys 
import re       
if len(sys.argv) == 1:
    print("none")
else: 
    string = sys.argv[1]
    z_count = re.findall(r"z", string)
    if z_count:
        for i in z_count:
            print ("z", end  = "")
        print (end = "\n")
    else:
        print ("none")