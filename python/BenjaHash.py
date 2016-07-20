#!/usr/bin/env python3

import convert

#Modulus_Always_PoSitive
def MAPS(value1, value2):
    if value1 > value2:
        return value1 % value2
    else:
        return value2 % value1

def HashLoop(binary):
    result = ""
    for i in range(0, len(binary), 2):
        try:
            result = result + str(MAPS(int(binary[i], 2),int(binary[i + 1], 2)))
        except ZeroDivisionError:
            #Do nothing if a division by zero error appears
            pass
        except IndexError:
            #Do nothing if an index error appears
            pass
    if len(result) < 1:
        result = "0"
    return(result)

def hash(source):
    result = HashLoop(source)

    while len(convert.intToBinary(result)) > 1:
        result = HashLoop(convert.intToBinary(result))

    return int(result)
