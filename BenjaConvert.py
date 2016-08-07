#!/usr/bin/env python3

def intToBinary(x):
    C = "{0:b}".format(int(x))
    C = binToArray(C)
    return C

def strToBinary(x):
    C = ''.join(format(ord(i), 'b') for i in x)
    C = binToArray(C)
    return C

def binToArray(x):
    C = [x[i:i+8] for i in range(0, len(x), 8)]
    return C
