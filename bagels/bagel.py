import random

NUM_DIGITS = 3
MAX_GUESS = 10


def getSecretNum():
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ' '
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return seceretNum


def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

        clues = []
        for i in range(len(guess)):
            if guess[i] == secretNum[i]:
                clues.append('Fermi')
            elif guess[i] in secretNum:
                clues.append('Pico')
        if len(clue) == 0:
            return 'Bagels'

        clues.sort()
        return ' '.join(clues)


def isOnlyDigits(num):
    if num == ' ':
        return False

        for i in num:
            if i not in '0 1 2 3 4 5 6 7 8 9'.split():
                return False

        return True


print('I am thinking of a number')
print('The clues I give are...')
print('When I say: That means: ')
print('Bagels None are correct')
print('Pico one is correct but in wrong position')
print('Fermi one is correct and in the right position')

while True:
    secretNum = getSecretNum()
    print('I have a number')

    guessesTaken = 1
    while guessesTaken <= MAX_GUESS:
        guess = ''
        while len(guess) != NUM_DIGITS:
            print((guessesTaken))
            guess = input()

        print(getClues(guess, secretNum))
        guessesTaken += 1

        if guess == secretNum:
            break
        if guessesTaken > MAX_GUESS:
            print('No more guesses')

    print('Do you want to play again')
    if not input().lower().startswith('y'):
        break
