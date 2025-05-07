#!/usr/bin/env python3

import sys

l = len(sys.argv)
if l > 3:
    for i in range(l):
        print(sys.argv[i])
else:
    print("none")