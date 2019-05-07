def introTutorial(V, arr):
    length = len(arr)
    left = 0
    right = length - 1
    while True:
      middle = round((left + right) / 2)
      if arr[middle] > V:
        right = max(middle - 1, 0)
      elif arr[middle] < V:
        left = min(middle + 1, length - 1)
      else: break
    return middle

print(introTutorial(23, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]))