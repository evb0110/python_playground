k = 3
contests = ((5, 1), (2, 1), (1, 1), (8, 1), (10, 0), (5, 0))

def luckBalance(k, contests):
  unimportant = [contest[0] for contest in contests if contest[1] == 0]
  important = [contest[0] for contest in contests if contest[1] == 1]
  sum_unimportant = sum(unimportant)
  important_sorted = sorted(important, reverse=True)
  important_plus = important_sorted[:k]
  important_minus = important_sorted[k:]
  sum_important_plus = sum(important_plus)
  sum_important_minus = sum(important_minus)
  return sum_unimportant + sum_important_plus - sum_important_minus



print(luckBalance(k, contests))