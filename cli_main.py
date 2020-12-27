#!/usr/bin/env python3

import sys
import os


options = [
    'Add New Account',
    'View Account',
    'Change Password for Account',
    'Remove Account',
    'Import Accounts from XML',
    'Export Accounts to XML',
    'Exit'
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
    elif cmd == 'Change Password for Account':
        pass
    elif cmd == 'Remove Account':
        pass
    elif cmd == 'Import Accounts from XML':
        pass
    elif cmd == 'Export Accounts to XML':
        pass
    elif cmd == 'Exit':
        exit()


if __name__ == '__main__':
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
