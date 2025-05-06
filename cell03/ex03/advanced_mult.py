#!/usr/bin/env python3

# this program will display all multiplication table
# use two while loops
import sys

if (len(sys.argv) == 1):
    i = 0
    j = 0
    while (i < 11):
        print(f"Table de {i}:", end= " ")
        while (j < 11):
            print(f"{i*j}", end= " ")
            j += 1
        j = 0
        i += 1
        print("")
else:
    print("none")






