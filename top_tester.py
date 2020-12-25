#!/usr/bin/env python3

import src.helpers as helpers
from src.locker import Locker as lock
import os, sys, json


if __name__ == '__main__':
    os.chdir(sys.path[0])

    keylocker = lock()
    helpers.printParamsDB()
    print()
    with open('bin/params_db.json') as f:
        keylocker.add(site='https://my.byu.edu', username='monka90', dict=json.load(f)['all_20'])
        print()
        keylocker.add(site='gmail.com', username='czech.monk90@gmail.com')