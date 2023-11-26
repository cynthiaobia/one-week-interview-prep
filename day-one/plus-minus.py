#!/bin/python3

# import math
# import os
# import random
# import re
# import sys


# rest of your code


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

'''
def plusMinus(arr):
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
'''

# loop thru. 
# if x > 0, increment pos
# if x == 0, increment zero
# if x < 0, increment neg
# float 6 decimals pos / arr length line break
# float 6 decimals zero / arr length line break
# float 6 decimals negative / arr length 

arr = [1, 1, 0, -1, -1]

zero = 0
pos = 0
neg = 0

for i in arr:
    if i > 0:
        pos += 1
    elif i < 0:
        neg += 1
    else:
        zero += 1

print(format(float(pos / len(arr)), '.6f'))
print(format(float(neg / len(arr)), '.6f'))
print(format(float(zero / len(arr)), '.6f'))


    
            

