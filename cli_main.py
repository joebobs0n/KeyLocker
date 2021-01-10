#!/usr/bin/python3

import sys, os


options = [
    'Add New Account',
    'View Account',
    'Generate New Password'
]


def printMenu():
    os.system('cls')
    mainTitle = 'KeyLocker CLI'
    print('+' + f''.ljust(98, '-') + '+')
    print('|' + f'{mainTitle}'.center(98, ' ') + '|')
    print('+' + f''.ljust(98, '-') + '+')
    for idx, opt in enumerate(options, start=1):
        print(f'    {idx:2d}: {opt}')

def switchAction(cmd):
    if cmd == 'Add New Account':
        pass
    elif cmd == 'View Account':
        pass
    elif cmd == 'Generate New Password':
        pass


if __name__ == '__main__':
    os.chdir(sys.path[0])

    while(1):
        printMenu()
        x = ''
        valid = True
        try:
            x = int(input('  >> ')) - 1
        except:
            valid = False
            print('Error:', sys.exc_info()[0])
            input()

        if valid == True:
            if x < len(options) and x >= 0:
                print(type(x), options[x])
                switchAction(options[x])
                input()

