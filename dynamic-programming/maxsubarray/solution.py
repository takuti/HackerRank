#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    max_subarray = max(arr)
    if max_subarray > 0:
        s = 0
        for a in arr:
            s = max(0, s + a)
            max_subarray = max(max_subarray, s)

    arr = sorted(arr)[::-1]
    max_subseq = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < 0:
            break
        max_subseq += arr[i]

    return [max_subarray, max_subseq]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input().strip())

    for t_itr in xrange(t):
        n = int(raw_input().strip())

        arr = map(int, raw_input().rstrip().split())

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
