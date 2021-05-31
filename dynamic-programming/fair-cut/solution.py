#!/bin/python

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'fairCut' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def unfairness(arr, I, J, th=-1):
    res = 0
    for i in I:
        for j in J:
           res += abs(arr[i] - arr[j])
           if th >= 0 and res > th:
               return th
    return res


def fairCut(k, arr):
    all_indices = set(range(len(arr)))
    min_unfairness = -1

    for c in combinations(all_indices, k):
        I = set(c)
        J = all_indices - I
        u = unfairness(arr, I, J, min_unfairness)
        min_unfairness = u if min_unfairness == -1 else min(min_unfairness, u)
    return min_unfairness


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = raw_input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = map(int, raw_input().rstrip().split())

    result = fairCut(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
