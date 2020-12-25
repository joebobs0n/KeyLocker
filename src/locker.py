#!/usr/bin/env python3

from src.passGen import PasswordGenerator as pg
from src.account import Account as ac

from pathlib import Path
import json


class Locker():
    def __init__(self):
        self.__params_db = Path('bin/params_db.json')
        if not self.__params_db.exists():
            with open(self.__params_db, 'w') as f:
                pass

        self.__accounts_list = Path('bin/accounts_list.txt')
        if not self.__accounts_list.exists():
            with open(self.__accounts_db, 'w') as f:
                pass

    def add(self, site, username, dict=None):
        # TODO: check if site already has an account
        # TODO: if it does, then check if it already has the same username
        # TODO: if it does, raise error and inform user
        # TODO: if it does not, create new account with same site

        params = dict
        if dict == None:
            with open('bin/params_db.json') as f:
                params = json.load(f)['default']

        generator = pg(params)
        new_pw = generator.generatePassword()
        account = ac(site, username, new_pw, params)
        ac_xml = account.toXML()

        print(ac_xml.attrib)
        print(ac_xml.attrib['password'])

        # TODO: encrypt information and write to file
        # TODO: if creating new account for existing site, append to file

    def access(self, site):
        username = ''
        password = ''

        return username, password

    def newPassword(self, site):
        pass

    def listSites(self):
        pass
