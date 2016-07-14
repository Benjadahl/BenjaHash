#!/usr/bin/env python3

import sys
import Hasher

if __name__ == '__main__':
    if sys.argv[1] == "string":
        print("String does not work yet")

    if sys.argv[1] == "int":
        source = "{0:b}".format(int(sys.argv[2]))
        source = [source[i:i+8] for i in range(0, len(source), 8)]
        Hasher.hash(source)
