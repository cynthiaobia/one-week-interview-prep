#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

# def diagonalDifference(arr):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     arr = []

#     for _ in range(n):
#         arr.append(list(map(int, input().rstrip().split())))

#     result = diagonalDifference(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()

# 3
# 11 2 4
# 4 5 6
# 10 8 -12

# let i = 0 index
# counter = 0
# sum_1 = 0 sum_2 = 0
# while i < (n -1)
# add to sum 1, go to next row by adding n to i
# do reverse for sum 2
# abs value of the difference

n = 3
arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

i = 0 # starting index at beginning of row
# find first diagonal sum
sum_1 = 0
for row in arr: 
    sum_1 += row[i]
    i += 1 #looping thru forward

j = -1 # starting index at end of row
# find second diagonal sum
sum_2 = 0
for row in arr:
    sum_2 += row[j]
    j -= 1 #looping thru backwards

difference = abs(sum_1 - sum_2)
print(difference)