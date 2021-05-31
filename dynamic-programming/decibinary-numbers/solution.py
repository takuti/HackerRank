#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'decibinaryNumbers' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER x as parameter.
#

def to_db(v):
    digits = str(v)
    res = 0
    for i in range(len(digits)):
        res += int(digits[i]) * 2**(len(digits)-1-i)
    return res


size = 9000
dbs = sorted([(to_db(i), i) for i in range(0, size)])


def decibinaryNumbers(x):
    return dbs[x-1][1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input().strip())

    for q_itr in xrange(q):
        x = int(raw_input().strip())

        result = decibinaryNumbers(x)

        fptr.write(str(result) + '\n')

    fptr.close()
