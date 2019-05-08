input = [1, 1, 3, 2, 1]

def countingSort(arr):
  freqs = [0 for i in range(100)]
  for el in arr:
    freqs[el] += 1
  res = []
  for i in range(100):
    res.extend([i] * freqs[i])
  return res

print(countingSort(input))