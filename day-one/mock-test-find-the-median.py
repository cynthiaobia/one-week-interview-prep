arr = [5, 3, 1, 2, 4, 1]

sorted_arr = sorted(arr)
print('sorted_arr: ', sorted_arr)
arr_len = len(arr)
print('arr_len: ', arr_len)

if len(arr) % 2 == 0:
  i = int(len(arr) / 2)
  print('index: ', i)
  median = (sorted_arr[i] + sorted_arr[i - 1]) / 2
  print('arr even')
else:
  i = int(len(arr) / 2)
  median = sorted_arr[i]
  print('index: ', i)
  print('arr odd')

print(int(median))