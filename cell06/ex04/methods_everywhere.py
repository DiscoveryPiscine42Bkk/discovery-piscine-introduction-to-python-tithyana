#!/usr/bin/env python3

import sys

def shrink(word : str) -> str:
    return word[:8]
def enlarge(word : str) -> str:
    l = len(word)
    while l < 8:
        word = word + 'Z'
        l += 1
    return word
l = len(sys.argv)
if l > 1:
    for i in range(1, l):
        if len(sys.argv[i]) > 8:
            print(shrink(sys.argv[i]))
        else:
            print(enlarge(sys.argv[i]))
else:
    print("none")
