#!/usr/bin/env python3

import sys
n = len(sys.argv)
if n > 1:
    for i in range(1, n):
        if sys.argv[i].endswith("ism"):
            pass
        else: 
            print(f"{sys.argv[i]}ism")
else:
    print("none")