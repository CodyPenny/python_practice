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



def computer_guess(x):
  computer_random = random.randint(1, 10)
  while x != computer_random:
    if(computer_random < x):
      print('comp guessed low')
    elif computer_random > x:
      print('comp guessed high')
    computer_random = random.randint(1, 10)
  print('comp guessed correct')

def computer_guess2(x):
  low: 1
  high: x
  feedback: ''
  while feedback != 'c':
    if low != high:
      guess = random.randint(low, high)
    else:
      guess = low # could also be high b.c low = high
    feedback = input(f'is {guess} too high (h), too low (l), or correct (c)').tolower()
    if feedback == 'h':
      high = guess - 1
    elif feedback == 'l':
      low = guess + 1

  print(f'hooray, the comp guessed your num, {guess}')

