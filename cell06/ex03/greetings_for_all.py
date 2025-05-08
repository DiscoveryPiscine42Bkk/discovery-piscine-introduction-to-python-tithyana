#!/usr/bin/env python3

def greetings(name = "noble stranger"):
    if str(name).replace(" ", "").isalpha():
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
