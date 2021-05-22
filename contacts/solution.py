#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#

def contacts(queries):
    dic = {}
    for op, val in queries:
        if op == 'add':
            for i in range(len(val)):
                k = val[:(i+1)]
                if k not in dic:
                    dic[k] = 0
                dic[k] += 1
        else:  # find
            yield 0 if val not in dic else dic[val]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(raw_input().strip())

    queries = []

    for _ in xrange(queries_rows):
        queries.append(raw_input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
