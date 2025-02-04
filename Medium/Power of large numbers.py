#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def solve(a, b):
    MOD = 10 ** 9 + 7
    a = int(a) % MOD
    b = int(b) % (MOD - 1)  # a^p % p = a for any prime number p

    res = 1
    while b > 0:
        if b % 2 == 1:
            res = res * a % MOD
        a = a * a % MOD
        b >>= 1  # right shift by one (equal to floor division by 2)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = first_multiple_input[0]

        b = first_multiple_input[1]

        result = solve(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
