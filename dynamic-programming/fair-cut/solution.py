#!/bin/python

import math
import os
import random
import re
import sys
from itertools import permutations

#
# Complete the 'fairCut' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def fairCut(k, arr):
    n = len(arr)
    k = min(k, n - k)
    arr = sorted(arr)  # make calculating abs easier

    # dp[i][j]: i-th number is processed, j = |I|
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(n):
        for j in range(i+1):
            I_size = j
            J_size = i - j

            if I_size > k or J_size > (n - k):
                continue

            # (1) assign arr[i] to I
            # Meaning, because arr[i] is ordered by ascending,
            #   (arr[i] - arr[_]) where _ < |J|, (arr[_] - arr[i]) where |J| < _ < n-k
            # = adding arr[i] from 1 to |J|, subtracting arr[i] for the rest
            unfairness_I = dp[i][j] + arr[i] * J_size - arr[i] * ((n - k) - J_size)

            # (2) assign arr[i] to J
            #   (arr[i] - arr[_]) where _ < |I|, (arr[_] - arr[i]) where |I| < _ < k
            # = adding arr[i] for |J|, subtracting arr[i] for the rest ((n-k) * |J|)
            unfairness_J = dp[i][j] + arr[i] * I_size - arr[i] * (k - I_size)

            dp[i+1][j+1] = min(dp[i+1][j+1], unfairness_I)
            dp[i+1][j] = min(dp[i+1][j], unfairness_J)  # |I| doesn't change; j = j

    return dp[n][k]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = raw_input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = map(int, raw_input().rstrip().split())

    result = fairCut(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
