#!/bin/python3

# Matrix Script Decoding problem provided by HackerRank.
# source (https://www.hackerrank.com/challenges/matrix-script/problem)

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)


#  --- Solution ---
newmatrix = []

for col in range(m):
    for row in range(n):
        newmatrix.append(matrix[row][col])

matrix = ''.join(newmatrix)

matrix2 = re.sub(r'(?<=\w)\W+(?=\w)', ' ', matrix)

print(matrix2)
