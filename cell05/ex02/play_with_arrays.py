#!/usr/bin/env python3

a = [2, 8, 9, 48, 8, 22, -12, 2]
b = []

for i in range(len(a)):
    if a[i] > 5:
        b.append(a[i] + 2)

print(f"Original array: {a}")
print(f"New array: {b}")