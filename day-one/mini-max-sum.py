#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'miniMaxSum' function below.
# #
# # The function accepts INTEGER_ARRAY arr as parameter.
# #

# def miniMaxSum(arr):
#     # Write your code here

# if __name__ == '__main__':

#     arr = list(map(int, input().rstrip().split()))

#     miniMaxSum(arr)

# order array in ascending order
# min sum of from 0 index to (array length - 2) indices
# reverse array and find max sum

arr = [3, 1, 5, 7, 9]
sorted_arr = sorted(arr)

min_sum = 0
i = 0
while (i < len(arr) - 1):
  min_sum += sorted_arr[i]  
  i += 1

max_sum = 0
sorted_arr.reverse()
j = 0
while (j < len(arr) - 1):
  max_sum += sorted_arr[j]  
  j += 1

print(sorted_arr)
print(min_sum)
print(max_sum)