#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER c
#

def solve(a, b, c):
    # according to Bezout's identity, you can find multiples of a and b such that their sum equals d if d is the greatest common denominator
    d = math.gcd(a, b)
    # f.e. (wlog a>b) let n be the smallest pos int s.t. a<nb.wew can obtain nb-a
    # and consequently 2nb-2a mod a
    if c <= max(a, b) and c % d == 0: return "YES"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        c = int(first_multiple_input[2])

        result = solve(a, b, c)

        fptr.write(result + '\n')

    fptr.close()
