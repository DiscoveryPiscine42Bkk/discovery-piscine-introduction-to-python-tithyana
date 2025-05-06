#!/usr/bin/env python3

# prompt for two numbers
a = int(input("Enter the first number: \n"))
b = int(input("Enter the second number: \n"))
print(f"{a} x {b} = {a*b}")
if a*b < 0:
    print("The result is negative.")
elif a*b > 0:
    print("The result is positive.")
else:
    print("The result is positive and negative.")