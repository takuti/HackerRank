#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def candies(n, arr):
    dp = [0] * n

    dp[0] = 1 if arr[0] <= arr[1] else 2

    for i in range(1, n):
        if arr[i-1] < arr[i]:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = 1

    for j in range(n-1, 0, -1):
        if arr[j-1] < arr[j] and dp[j-1] >= dp[j]:
            dp[j] = dp[j-1] + 1
        elif arr[j-1] > arr[j] and dp[j-1] <= dp[j]:
            dp[j-1] = dp[j] + 1

    return sum(dp)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    arr = []

    for _ in xrange(n):
        arr_item = int(raw_input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
