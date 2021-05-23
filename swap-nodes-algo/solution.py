#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

def swapNodes(indexes, queries):
    for k in queries:
        # swap
        parent_to_children = {1: [1]}
        d = 2
        while True:
            nodes = set(parent_to_children[d-1])
            if -1 in nodes:
                nodes.remove(-1)
            parent_to_children[d-1] = nodes
            if len(nodes) == 0:
                break

            children = []
            for node in nodes:
                children += indexes[node-1]
            parent_to_children[d] = children

            d += 1

        h = k
        while h in parent_to_children:
            for node in parent_to_children[h]:
                indexes[node-1] = indexes[node-1][::-1]
            h += k

        # traverse
        traverse = [1]
        visited = set()
        for _ in range(len(indexes)):
            n_traverse = len(traverse)
            for i in range(n_traverse):
                node = traverse[i]
                if (node != -1) and (node not in visited):
                    left, right = indexes[node-1]
                    traverse = traverse[:i] + [left, node, right] + traverse[i+1:]
                    visited.add(node)
                    break
        yield [node for node in traverse if node != -1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    indexes = []

    for _ in xrange(n):
        indexes.append(map(int, raw_input().rstrip().split()))

    queries_count = int(raw_input().strip())

    queries = []

    for _ in xrange(queries_count):
        queries_item = int(raw_input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
