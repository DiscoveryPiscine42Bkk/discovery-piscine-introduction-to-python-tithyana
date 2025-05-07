#!/usr/bin/env python3

import sys

l = len(sys.argv)
if l == 2:
    print(sys.argv[1].lower())
else:
    print("none")