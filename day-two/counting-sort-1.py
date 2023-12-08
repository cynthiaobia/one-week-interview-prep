#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# def countingSort(arr):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     result = countingSort(arr)

#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()


arr = [1, 1, 3, 2, 1]
# arr.sort()
# int_range = arr[-1] # finding largest int

frequency_arr = []

# counting occurrence at each index
for i in range(100):
  frequency_arr.append(arr.count(i))

print(frequency_arr)