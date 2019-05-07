from random import randint

to_play = 'y'

while to_play == 'y':
  rand = randint(1, 10)
  print('')
  while True:
    answer = input("what's your guess? ")
    answer = int(answer)
    if answer < rand:
      print('too low')
    elif answer > rand:
      print('too high')
    else:
      print('you guessed it!\n')
      break


  to_play = input('do you want to play once more (y/n) ')