#!/bin/python

import math
import os
import random
import re
import sys


class PriorityQueue(object):

    def __init__(self):
        self.q = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return i * 2 + 1

    def right(self, i):
        return i * 2 + 2

    def up(self, i):
        j = self.parent(i)
        while (i > 0 and self.q[j] > self.q[i]):
            self.q[i], self.q[j] = self.q[j], self.q[i]
            i, j = j, self.parent(j)

    def down(self, i):
        k = i

        l = self.left(i)
        if l < len(self.q) and self.q[l] < self.q[k]:
            k = l

        r = self.right(i)
        if r < len(self.q) and self.q[r] < self.q[k]:
            k = r

        if k != i:
            self.q[i], self.q[k] = self.q[k], self.q[i]
            self.down(k)

    def push(self, e):
        self.q.append(e)
        self.up(len(self.q) - 1)

    def pop(self):
        e = self.q[0]
        self.q[0] = self.q[-1]
        del self.q[-1]
        self.down(0)
        return e

    def __len__(self):
        return len(self.q)


#
# Complete the 'minimumAverage' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY customers as parameter.
#

def minimumAverage(customers):
    customers = sorted(customers)

    t = customers[0][0]  # first customer's arrival time
    queue = PriorityQueue()
    for c in customers:
        if c[0] == t:
            queue.push(c[::-1])
    cnt = len(queue)

    accum_waiting = 0

    while len(queue) != 0:
        c = queue.pop()[::-1]

        t += c[1]  # add time to cook
        accum_waiting += t - c[0]

        if cnt < len(customers):
            if t < customers[cnt][0] and len(queue) == 0:
                t = customers[cnt][0]
            if t >= customers[cnt][0]:
                for c in customers[cnt:]:
                    if c[0] <= t:
                        queue.push(c[::-1])
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
