#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    if sys.argv[1] == "string":
        print("String does not work yet")

    if sys.argv[1] == "int":
        source = "{0:b}".format(int(sys.argv[2]))
        print(source)
