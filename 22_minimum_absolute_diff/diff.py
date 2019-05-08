input = [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]

def minimumAbsoluteDifference(arr):
  arr.sort()
  res = float('inf')
  for i in range(len(arr) - 1):
    diff = arr[i + 1] - arr[i]
    if res > diff:
      res = diff
  return res

print(minimumAbsoluteDifference(input))