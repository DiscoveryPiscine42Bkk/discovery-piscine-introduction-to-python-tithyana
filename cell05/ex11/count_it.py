#!/usr/bin/env python3

import sys

n = len(sys.argv)
if n > 1:
    print(f"parameters: {n -1}")
    for i in range(1, n):
        print(f"{sys.argv[i]}: {len(sys.argv[i])}")
else:
    print("none")