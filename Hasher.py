#!/usr/bin/env python3

def hash(source):
    for i in range(0, len(source), 2):
        print(i)
        print(str(int(source[i], 2) % int(source[i + 1], 2)))
