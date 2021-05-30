#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def abbreviation(a, b):
    if a.upper() == b:
        return 'YES'
    if len(a) == 0 and len(b) > 0:
        return 'NO'

    is_lower = lambda c: 'a' <= c and c <= 'z'

    n_upper = sum([not is_lower(c) for c in a])
    if n_upper > len(b):
        return 'NO'

    dp = [[False] * (len(b) + 1) for _ in range(len(a) + 1)]

    dp[0][0] = True
    for i in range(1, len(a) + 1):
        dp[i][0] = (dp[i-1][0] and is_lower(a[i-1]))

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if is_lower(a[i-1]):
                # delete or capitalize
                dp[i][j] = (dp[i-1][j] or (dp[i-1][j-1] and (a[i-1].upper() == b[j-1])))
            else:
                dp[i][j] = (dp[i-1][j-1] and (a[i-1] == b[j-1]))
    return 'YES' if dp[-1][-1] else 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input().strip())

    for q_itr in xrange(q):
        a = raw_input()

        b = raw_input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
