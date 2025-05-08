#!/usr/bin/env python3

import sys
#argument vector
if (len(sys.argv) == 2):
    word = input("What was the parameter? ")
    if (word != sys.argv[1]):
        print("Nope, sorry...")
    else:
        print("Good job!")
else:
    print("none")