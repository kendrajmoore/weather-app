SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
MAX_KEY_SIZE = len(SYMBOLS)


def getMode():
    while True:
        print('Do you wish to encrypt or decrypt a message')
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd']:
            return mode
        else:
            print('Enter encrypt or e or decrypt or d')


def getMessage():
    print('Enter your message: ')
    return input()


def getKey:
    key = 0
    while True:
        print('Enter the key number (1 -%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 )
