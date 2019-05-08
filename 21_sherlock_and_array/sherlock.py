input = [2]

def balancedSums(arr):
  if len(arr) == 1:
    return 'YES'
  i = 0
  left = 0
  right = sum(arr[1:])
  while (i < len(arr) - 1):
    if left == right:
      return 'YES'
    left += arr[i]
    right -= arr[i + 1]
    i += 1
  return 'NO'


print(balancedSums(input))