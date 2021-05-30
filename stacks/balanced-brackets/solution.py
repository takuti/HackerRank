#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    stack = []
    pairs = {'}': '{', ']': '[', ')': '('}
    closure = pairs.keys()
    for c in s:
        if c in closure:
            if len(stack) == 0:
                return 'NO'
            c_top = stack.pop(-1)
            if c_top != pairs[c]:
                return 'NO'
        else:
            stack.append(c)
    return 'YES' if len(stack) == 0 else 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input().strip())

    for t_itr in xrange(t):
        s = raw_input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
