#!/usr/bin/env python3

import sys

l = len(sys.argv)
c = 0
if l == 3:
    a = sys.argv[1] #keyword
    b = sys.argv[2] #string
    #search for the keyword inside the string
    c = b.count(a)
    if c != 0:
        print(c)
    else:
        print("none")
else:
    print("none")

