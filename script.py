#!/usr/bin/env python3
import random

#############################################
# This functions takes in a filepath and    #
# adds numbers for memory initialization.   #
# The numbers are added in hex so user can  #
# read this with a readmemh command.        #
#############################################

def randGen (filepath, addr_bits, num_bytes):
    fh = open(filepath, "w")
    lines = 2 ** addr_bits
    for line in range(lines):
        print_str = ""
        for bytes in range(num_bytes):
            print_str += hex(random.randrange(0, 16))[2:]
        fh.write(print_str + "\n")
    fh.close()

if __name__ == '__main__':
    randGen("./test.txt", 10, 2)