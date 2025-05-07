#!/usr/bin/env python3

a = [2, 8, 9, 48, 8, 22, -12, 2]
c = set()
for i in range(len(a)):
    if a[i] > 5:
        c.add(a[i] + 2)
print(a)
print(c)