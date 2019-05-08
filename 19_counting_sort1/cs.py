input = [1, 1, 3, 2, 1]

def countingSort(arr):
  result = [0 for i in range(100)]
  for el in arr:
    result[el] += 1
  return result



countingSort(input)