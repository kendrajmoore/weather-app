import random

NUM_DIGITS = 3
MAX_GUESS = 10


def getSecretNum():
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ' '
    for i in range(numDigits):
        secretNum += str(numbers[i])
    return seceretNum


def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

        clue = []

        for i in range(len(guess)):
            if guess[i] == secretNum[i]:
                clue.append('Fermi')
            elif guess[i] in secretNum:
                clue.append('Pico')
        if len(clue) == 0:
            return 'Bagels'

        clue.sort()
        return ' '.join(clue)


def isOnlyDigits(num):
    if num == ' ':
        return False

        for i in num:
            if i not in '0 1 2 3 4 5 6 7 8 9'.split():
                return False

        return True


def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


NUMDIGITS = 3
MAXGUESS = 10

print(I am thinking of a number)
