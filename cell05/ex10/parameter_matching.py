#!/usr/bin/env python3

import sys

if (len(sys.argv) == 1):
    print("none")
else:
    word = input("What was the parameter? ")
    if (word != sys.argv[1]):
        print("Nope, sorry...")
    else:
        print("Good job!")