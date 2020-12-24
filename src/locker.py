#!/usr/bin/env python3

from pathlib import Path


class Locker():
    def __init__(self, params_db_path='bin/params_db.json'):
        self.__params_db = Path(params_db_path)
        print(self.__params_db.exists())


if __name__ == '__main__':
    foo = Locker(params_db_path='../bin/params_db.json')
