#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isFibo' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def isFibo(n):
    a = (5*(n**2)+4)
    b = (5*(n**2)-4)
    if int(a**.5)**2 == a or int(b**.5)**2 == b: return "IsFibo"
    return "IsNotFibo"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = isFibo(n)

        fptr.write(result + '\n')

    fptr.close()
