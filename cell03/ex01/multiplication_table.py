#!/usr/bin/env python3

print("Enter a number")
n = int(input())
def table():
    for i in range(10):
        print(f"{i} x {n} = {i*n}")
table()