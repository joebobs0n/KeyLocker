#!/usr/bin/env python3

from src.locker import Locker as lock
import os, sys, json


if __name__ == '__main__':
    os.chdir(sys.path[0])

    keylocker = lock()
    f = open('bin/params_db.json')
    params_db = json.load(f)

    print(keylocker.add(site='https://my.byu.edu', username='monka90', params=params_db['all_20']))
    print(f'  > {json.dumps(keylocker.access("my.byu"))}')
    print(keylocker.add(site='www.gmail.com', username='czech.monk90@gmail.com'))
    print(f'  > {json.dumps(keylocker.access("gmail"))}')
    print(keylocker.add(site='www.gmail.com', username='circuit.monk90@gmail.com'))
    print(f'  > {json.dumps(keylocker.access("gmail"))}')
    print(keylocker.newPassword('www.gmail.com', username='czech.monk90@gmail.com'))
    print(f'  > {json.dumps(keylocker.access("gmail"))}')
    print(keylocker.newParams('gmail.com', 'czech.monk90@gmail.com', params_db['min_punct_20']))
    print(f'  > {json.dumps(keylocker.access("gmail"))}')