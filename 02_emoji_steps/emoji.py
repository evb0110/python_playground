# for row in range(10):
#   print("\U0001f600 "  * (row + 1))

row = 0;
while row < 10:
  row += 1
  print(' ' * (11 - row) + "\U0001f600 "  * row)

# for num in range(10):
#   smyleys = ''
#   for cnt in range(num+1):
#     smyleys += "\U0001f600 "
#   print(smyleys)
