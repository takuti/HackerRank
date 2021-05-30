#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def runningMedian(a):
    medians = [a[0]]
    for n in range(2, len(a) + 1):
        l = sorted(a[:n])
        mid = n // 2
        if n % 2 == 0:
            medians.append((l[mid-1] + l[mid]) / 2.0)
        else:
            medians.append(l[mid])
    return medians

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(raw_input().strip())

    a = []

    for _ in xrange(a_count):
        a_item = int(raw_input().strip())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

