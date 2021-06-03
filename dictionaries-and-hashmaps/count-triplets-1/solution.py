#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    former, latter = {}, {}
    for a in arr:
        if a not in former:
            former[a] = 0

        if a not in latter:
            latter[a] = 0
        latter[a] += 1

    s = 0
    for a in arr:
        latter[a] -= 1

        f = a // r
        l = a * r
        if a % r == 0 and f in former and l in latter:
            s += former[f] * latter[l]

        former[a] += 1

    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = raw_input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = map(long, raw_input().rstrip().split())

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
