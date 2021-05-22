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
    names = []
    for op, val in queries:
        if op == 'add':
            names.append(val)
        else:  # find
            yield sum(map(lambda n: n.startswith(val), names))


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
