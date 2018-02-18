import random

ticVariable = ()

print('The computer will go first')

print('What is your next move?')

print('What is your next move?')

print('What is your next move?')

print('Do you want to play again?')


def drawBoard():
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Welcome to Tic-Tac-Toe! Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return['O', 'X']


def whoGoesFirst():
    if random.randit == 0:
        return 'computer'
    else:
        return 'player'


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le)
            (bo[4] == le and bo[5] == le and bo[6] == le)
            (bo[1] == le and bo[2] == le and bo[3] == le)
            (bo[7] == le and bo[4] == le and bo[1] == le)
            (bo[8] == le and bo[5] == le and bo[2] == le)
            (bo[9] == le and bo[6] == le and bo[3] == le)
            (bo[7] == le and bo[5] == le and bo[3] == le)
            (bo[9] == le and bo[5] == le and bo[1] == le))


def getBoardCopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    return board[move] == ''


def getPlayerMove(board):
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or 

def playAgain():
    pass
