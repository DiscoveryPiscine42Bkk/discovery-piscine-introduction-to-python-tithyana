#!/usr/bin/env python3

def array_of_names(d : dict) -> list:
    a = []
    for k, v in d.items():
        a.append(f"{k.capitalize()} {v.capitalize()}")
    return a

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))