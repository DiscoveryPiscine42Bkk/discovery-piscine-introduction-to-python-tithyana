#!/usr/bin/env python3

import sys

n = len(sys.argv)
if n == 2:
    count = 0
    # check each character in the parameter
    for i in sys.argv[1]:
        if i == "z":
            count += 1
    if count > 0:
        print("z" * count)
    else:
        print("none")
else:
    print("none")
