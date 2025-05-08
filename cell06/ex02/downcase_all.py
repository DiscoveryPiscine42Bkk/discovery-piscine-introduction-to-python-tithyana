#!/usr/bin/env python3

import sys

def downcase_it(s):
    return s.lower()

l = len(sys.argv)
if l > 1:
    for i in range(1, l):
        print(downcase_it(sys.argv[i]))
else:
    print("none")