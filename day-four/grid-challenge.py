


grid = ['xfg', 'abc', 'aze']

grid = ['eabcd', 'fghij', 'olkmn', 'trpqs', 'xywuv']

# for each item in arr, split into array and sort, then rejoin

sorted_arr = []
for row in grid:
  sorted_row = [*row]
  sorted_row.sort()
  sorted_str = ''.join(sorted_row)
  sorted_arr.append(sorted_str)

print(sorted_arr)

asc_order = True

col = []
i = 0

while i < len(sorted_arr) and asc_order == True:
  for row in sorted_arr:
    col.append(row[i])
  print(col)
  sorted_col = sorted(col)
  if col == sorted_col:
    asc_order = True
  else:
    asc_order = False
  col = []
  print(col)
  i += 1

if asc_order == True:
  answer = 'YES'
else:
  answer = 'NO'

print(answer)
