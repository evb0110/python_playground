input = [4, 5, 3, 7, 2]

def quickSort(arr):
  pivot = arr[0]
  left = [val for val in arr if val < pivot]
  right = [val for val in arr if val > pivot]
  equal = [val for val in arr if val == pivot]
  return left + equal + right

print(quickSort(input))