#!/usr/bin/env python3

import json


def printParamsDB():
    with open('bin/params_db.json') as f:
        available_dicts = json.load(f)
        for dict in list(available_dicts):
            print(f'{dict} '.ljust(18, '.'), f'{available_dicts[dict]}')
