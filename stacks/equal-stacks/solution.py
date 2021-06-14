#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    s1, s2, s3 = sum(h1), sum(h2), sum(h3)

    while len(h1) != 0 and len(h2) != 0 and len(h3) != 0:
        if s1 == s2 and s1 == s3:
            return s1

        if s1 > s2 and s1 > s3:
            s1 -= h1.pop(0)
        elif s2 > s1 and s2 > s3:
            s2 -= h2.pop(0)
        elif s3 > s1 and s3 > s2:
            s3 -= h3.pop(0)
        elif s1 == s2 and s1 > s3:
            s1 -= h1.pop(0)
            s2 -= h2.pop(0)
        elif s2 == s3 and s2 > s1:
            s2 -= h2.pop(0)
            s3 -= h3.pop(0)
        else:  # s3 == s1 and s3 > s2
            s3 -= h3.pop(0)
            s1 -= h1.pop(0)

    return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = raw_input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = map(int, raw_input().rstrip().split())

    h2 = map(int, raw_input().rstrip().split())

    h3 = map(int, raw_input().rstrip().split())

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
