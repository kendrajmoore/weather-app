'''My amazing dragon game'''

import random
import time


def displayIntro():
    print('''You are in a land full of dragons. In front of you, you see two
    ''')


print()


def cave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave do you choose (1 or 2)')
        cave = input()

    return cave


def badCave(cave):
    print('You approach the cave....')
    time.sleep(2)
    print('It is dark ....')
    time.sleep(2)
    print('You see a dragon')
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if cave == str(friendlyCave):
        print('Gives you money')
    else:
        print('You die')


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    cave()
    badCave(cave)

    print('Do you want to play again (yes or no)')
    playAgain = input()
