import random

def guess(x):
  random_num = random.randint(1, x)
  guess = 0
  while (guess != random_num):
    guess = int(input(f'Guess a number between 1 and {x}: '))
    if guess < random_num:
      print('sorry guess again, too low')
    elif guess > random_num:
      print('sorry, guess again, too high')
  print(f'congrats, you have guessed the num {random_num}')

guess(10)