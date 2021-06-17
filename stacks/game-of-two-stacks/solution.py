#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#

def twoStacks(maxSum, a, b):
    s = 0
    i = 0
    while i < len(a) and s + a[i] <= maxSum:
        s += a[i]
        i += 1
    res = i

    j = 0
    while j < len(b) and i >= 0:
        s += b[j]
        j += 1
        while s > maxSum and i >= 0:
            i -= 1
            s -= a[i]
        if s <= maxSum:
            res = max(res, i + j)

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(raw_input().strip())

    for g_itr in xrange(g):
        first_multiple_input = raw_input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = map(int, raw_input().rstrip().split())

        b = map(int, raw_input().rstrip().split())

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
