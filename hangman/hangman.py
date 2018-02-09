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


def printWord(wordList):
    wordIndex = random.randint(0, len(word) - 1)
    return wordList[wordIndex]


def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters: ', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()
