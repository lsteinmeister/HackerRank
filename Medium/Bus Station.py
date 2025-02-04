#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def solve(a):
    # a bus can always carry all passengers
    Sa = sum(a)
    # seats = [1]
    # find additional ways to evenly break up the group
    # find all divisors
    a_cs = []
    c_sum = 0
    for ca in a:
        c_sum += ca
        if Sa % c_sum == 0:
            a_cs.append(c_sum)

    bus_sizes = []
    for x in a_cs:
        count = 0
        check = True
        for pgr in a:
            count += pgr
            if count == x:
                count = 0
            elif count > x:
                check = False
                break
        if not check: continue
        bus_sizes.append(x)
    bus_sizes.sort()
    return bus_sizes


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
