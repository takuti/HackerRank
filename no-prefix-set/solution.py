#!/bin/python

import math
import os
import random
import re
import sys


class Chain(object):

    def __init__(self):
        self.root = {}

    def add(self, s):
        chain = self.root
        bad = False
        for c in s:
            if c not in chain:
                chain[c] = {}
            chain = chain[c]
            if '-' in chain:
                bad = True
        if len(chain) > 0:
            bad = True
        chain['-'] = None  # tail
        return bad


#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

def noPrefix(words):
    chain = Chain()
    for w in words:
        if chain.add(w):
            print('BAD SET')
            print(w)
            return
    print('GOOD SET')


if __name__ == '__main__':
    n = int(raw_input().strip())

    words = []

    for _ in xrange(n):
        words_item = raw_input()
        words.append(words_item)

    noPrefix(words)
