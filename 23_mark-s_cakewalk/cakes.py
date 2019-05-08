input = [5, 10, 7]

def marcsCakewalk(calories):
  sortedCalories = sorted(calories, reverse=True)
  total = 0
  for i in range(len(sortedCalories)):
    total += sortedCalories[i] * 2 ** i
  return total

print(marcsCakewalk(input))