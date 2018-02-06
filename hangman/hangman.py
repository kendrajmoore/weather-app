import random
HANGMAN_PICS = ['''

  +---+
      |
      |
      |
     ===''', '''
  +---+
 o    |
      |
      |
     === ''', '''
  +---+
  o   |
  |   |
      |
     === ''', '''
 +---+
 o   |
/|   |
     |
    === ''', '''
 +---+
 o   |
/|\  |
     |
    === ''', '''
 +---+
 o   |
/|\  |
/    |
    === ''', '''
 +---+
 o   |
/|\  |
/ \  |
    === ''']
word = 'ant baboon badger bat bear beaver camel cat clam'.split()

print('Missed letters: ')
