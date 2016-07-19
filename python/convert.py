#!/usr/bin/env python3

def intToBinary(arg):
        C = "{0:b}".format(int(arg))
        C = [C[i:i+8] for i in range(0, len(C), 8)]
        return C
