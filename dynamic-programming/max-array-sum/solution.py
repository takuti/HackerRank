#!/bin/python

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    for i in range(len(arr)):
        if i == 0:
            arr[i] = max(0, arr[0])
        elif i == 1:
            arr[i] = max(arr[0], arr[1])
        else:
            arr[i] = max(arr[i-1], arr[i] + arr[i-2])
    return arr[-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
