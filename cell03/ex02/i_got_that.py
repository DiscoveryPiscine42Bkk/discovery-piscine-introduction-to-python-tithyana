#!/usr/bin/env python3
# create a while loop with break
# it breaks when the response input is "STOP"

def response():
    a = input("What you gotta say? : ")
    while True:
        b = input("I got that! Anything else? : ")
        if b == "STOP":
            break
response()
