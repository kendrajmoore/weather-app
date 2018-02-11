import random

random_number = random.randint(1, 10)

while True:
    answer = input('Guess a number between 1 and 10: ')
    answer = int(answer)
    if answer > random_number:
        print('Too high, please try again')
    elif answer < random_number:
        print('Too low, please try again')
    else:
        print('You win!')
        play_again = input('Do you want to play again(y/n)')
        if play_again == 'y':
            random_number = random.randint(1, 10)
            answer = None
        else:
            print('Thank you for playing')
            break
