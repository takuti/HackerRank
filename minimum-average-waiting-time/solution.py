#!/bin/python

import math
import os
import random
import re
import sys
from heapq import heappush, heappop

#
# Complete the 'minimumAverage' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY customers as parameter.
#

def minimumAverage(customers):
    customers = sorted(customers)

    t = customers[0][0]  # first customer's arrival time
    queue = []
    for c in customers:
        if c[0] == t:
            heappush(queue, c[::-1])
    cnt = len(queue)

    accum_waiting = 0

    while len(queue) != 0:
        c = heappop(queue)[::-1]

        t += c[1]  # add time to cook
        accum_waiting += t - c[0]

        if cnt < len(customers):
            if t < customers[cnt][0] and len(queue) == 0:
                t = customers[cnt][0]
            if t >= customers[cnt][0]:
                for c in customers[cnt:]:
                    if c[0] <= t:
                        heappush(queue, c[::-1])
                        cnt += 1

    return accum_waiting // cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    customers = []

    for _ in xrange(n):
        customers.append(map(int, raw_input().rstrip().split()))

    result = minimumAverage(customers)

    fptr.write(str(result) + '\n')

    fptr.close()
