#!/bin/python3

import math
import os
import random
import re
import sys
from string import ascii_lowercase


#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    hash_map = {letter: height for letter, height in zip(ascii_lowercase, h)}
    max_height = 0
    for letter in word:
        current_height = hash_map.get(letter, 0)
        if current_height > max_height:
            max_height = current_height
    return max_height * len(word)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
