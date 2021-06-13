#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    stack = []
    res = []
    max_in_stack = 0
    for op in operations:
        lst = op.split(' ')
        o = lst[0]
        if o == '1':  # 1 x
            val = int(lst[1])
            stack.append(val)
            if val > max_in_stack:
                max_in_stack = val
        elif o == '2':  # 2
            val = stack.pop(-1)
            if val == max_in_stack:
                max_in_stack = 0 if len(stack) == 0 else max(stack)
        else:  # 3
            res.append(max_in_stack)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    ops = []

    for _ in xrange(n):
        ops_item = raw_input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
