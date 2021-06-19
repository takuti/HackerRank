#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    res = 0
    for i in range(len(h)):
        k = 1
        h_min = h[i]
        res = max(res, h_min)
        for j in range(i+1, len(h)):
            k += 1
            h_min = min(h_min, h[j])
            res = max(res, h_min * k)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    h = map(int, raw_input().rstrip().split())

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
