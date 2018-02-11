import random

random_number = random.randit(1, 11)

answer = input('Guess a number between 1 and 10: ')

if answer > random_number:
    print('Too high, please try again')
if answer < random_number:
    print('Too low, please try again')
else:
    print('You win!')
