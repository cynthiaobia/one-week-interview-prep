

# Test Case 0
n = '148' 
k = 3

# # Test Case 1
# n = '9875'
# k = 4

# # Test Case 2
# n = '123'
# k = 3

p = n * k 
# print('full number p: ', p)

num_arr = [*p] # arr of digits as strings
num_arr = [eval(i) for i in num_arr] # convert str to int
# print('initial arr of digits: ', num_arr)

arr_sum = 0 # sum of digits in arr

count = len(num_arr) - 1 # num of digits

# loop until 1 digit is left
while count > 1:
  for i in num_arr:
    arr_sum += int(i)
  # print('Sum of digits: ', arr_sum)
  num_arr = [*str(arr_sum)] # convert digits in sum to arr as strings
  # print('current digits: ', num_arr)
  count = len(num_arr)
  # print('Arr length: ', count)
  arr_sum = 0

# print('final sum as arrary: ', num_arr)

for i in num_arr:
  super_digit = int(i)

print(super_digit)
