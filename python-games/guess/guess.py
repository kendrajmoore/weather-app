import random

guessesTaken = 0

number = random.randint(1, 20)


print('Hello what is your name?')

name = input()

print('I am thinking of a number between 1 and 20')

for guessesTaken in range(6):
    print('Take a guess')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low')

    if guess > number:
        print('Your guess is too high')

    if guess == number:
        break

if guess == number:
    print("Good job")
