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
            print("zero error")
        except IndexError:
            print("index error")
    if len(result) < 1:
        result = "0"
    return(result)

def hash(source):
    print(source[1])
    result = HashLoop(source)

    while len(convert.intToBinary(result)) > 1:
        print("len " + str(len(convert.intToBinary(result))))
        result = HashLoop(convert.intToBinary(result))
        print("res " + str(result))

    print("Result of the hash was: " + result)
