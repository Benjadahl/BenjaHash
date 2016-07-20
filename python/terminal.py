#!/usr/bin/env python3

import sys
import BenjaHash
import convert

if __name__ == '__main__':
    if sys.argv[1] == "string":
        print("String does not work yet")

    if sys.argv[1] == "int":
        source = convert.intToBinary(sys.argv[2])
        hashResult = BenjaHash.hash(source)

    if sys.argv[1] == "bin":
        source = convert.binToArray(sys.argv[2])
        hashResult = BenjaHash.hash(source)

    print("The result of the hash was: " + str(hashResult))
