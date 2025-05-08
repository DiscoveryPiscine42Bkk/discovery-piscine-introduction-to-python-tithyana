#!/usr/bin/env python3

import sys

l = len(sys.argv)
if l == 3:
    a = []
    for i in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
        a.append(i)
    print(a)
else:
    print("none")