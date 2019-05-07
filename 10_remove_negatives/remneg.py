def remove_negatives(nums):
  return list(filter(lambda num: num >= 0, nums))

print(
  remove_negatives([9, -3, 4, -4])
)