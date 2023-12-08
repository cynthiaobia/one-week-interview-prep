#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'timeConversion' function below.
# #
# # The function is expected to return a STRING.
# # The function accepts STRING s as parameter.
# #

# def timeConversion(s):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = timeConversion(s)

#     fptr.write(result + '\n')

#     fptr.close()

# check for AM or PM
# if AM, if 12, convert to 00, strip last two indices
# if PM, add 11, strip last two indices

time = '12:13:45AM'
# time = '01:13:45PM'
time = '07:05:45PM'
time = '12:45:54PM'

if time[-2:] == 'AM':
  new_time = time[0:-2] # strip AM
  if time[0:2] == '12':
    new_time = '00' + new_time[2:] # join with rest of arr
else:
  if time[0:2] == '12':
    new_time = time[0:-2]
  else:
    new_time = time[0:-2] # strip PM
    prefix = int(time[0:2]) + 12 # add 12
    new_time = str(prefix) + new_time[2:]

print(new_time)



