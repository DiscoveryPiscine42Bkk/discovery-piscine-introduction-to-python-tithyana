#!/usr/bin/env python3

def average(d : dict) -> float:
    sum = 0
    count = 0
    for v in d.items(): #or for k, v in d.items()
        sum += v[1]  #or sum += v
        count += 1
    return sum/count
class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}
class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")