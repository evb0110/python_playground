for n in range(1, 21):
  if n == 4 or n == 13:
    string = 'unlucky'.upper()
  elif n % 2:
    string = 'odd'
  else:
    string = 'even'
  print(f'{n}: {string}')