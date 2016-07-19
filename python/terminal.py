#!/usr/bin/env python3

import sys
import BenjaHash
import intToBinary

if __name__ == '__main__':
    if sys.argv[1] == "string":
        print("String does not work yet")

    if sys.argv[1] == "int":
        source = intToBinary.convert(sys.argv[2])
        BenjaHash.hash(source)
