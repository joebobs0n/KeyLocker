#!/usr/bin/python3

from src.passGen import PasswordGenerator as pg

from pathlib import Path
from cryptography.fernet import Fernet
import json, re, os


def siteCleaner(site):
    possible_tld = ''
    site_cleaned = site

    tld_path = Path('bin/domains')
    if not tld_path.exists():
        with open(tld_path, 'w') as f:
            f.write('com\norg\nio\nedu')

    with open(tld_path) as f:
        possible_tld = f.read()
    possible_tld = re.split('\n|\ ', possible_tld)
    possible_tld = [tld for tld in possible_tld if tld != '']
    possible_tld = '|'.join(possible_tld)

    http_found = re.finditer(f'^(http(s)?://)?(www\.)?', site)
    for remove in http_found:
        site_cleaned = site_cleaned.replace(remove[0], '')

    tld_found = re.finditer(f'\.({possible_tld}).*', site)
    for remove in tld_found:
        site_cleaned = site_cleaned.replace(remove[0], '')
    site_cleaned = site_cleaned.lower()

    return site_cleaned


class Locker():
    def __init__(self):
        self.__data = Path('data')
        self.__key = self.__data / 'key.key'
        self.__encoding = 'utf-8'

        if not self.__key.exists():
            key = Fernet.generate_key()
            with open(self.__key, 'wb') as f:
                f.write(key)

    def __loadKey(self):
        with open(self.__key, 'rb') as f:
            return f.read()

    def __writeEncryptedData(self, path, data):
        site_encoded = data.encode(self.__encoding)
        site_encrypted = Fernet(self.__loadKey()).encrypt(site_encoded)

        with open(path, 'wb') as f:
            f.write(site_encrypted)

    def __readEncryptedData(self, path):
        with open(path, 'rb') as f:
            data_encrypted = f.read()

        data_decrypted = Fernet(self.__loadKey()).decrypt(data_encrypted)
        return data_decrypted.decode(self.__encoding)

    def __loadSiteDictionary(self, site, username):
        site_cleaned = siteCleaner(site)
        site_path = self.__data / site_cleaned
        site_dict = {}
        userExists = False

        if site_path.exists():
            site_dict = self.access(site_cleaned)
            try:
                site_dict[username]
                userExists = True
            except KeyError as err:
                pass

        return site_dict, userExists, site_cleaned

    def __getLogin(self):
        pass

    def access(self, site):
        site_cleaned = siteCleaner(site)
        data_str = self.__readEncryptedData(self.__data / site_cleaned)
        data_json = json.loads(data_str)

        return data_json

    def add(self, site, username, params=None, pw_curr=None):
        site_dict, userExists, site_cleaned = self.__loadSiteDictionary(site, username)
        if userExists:
            return f'Account using {username} for {site} already exists'

        if params == None:
            with open('bin/params_db.json') as f:
                params = json.load(f)['default']

        generator = pg(params)
        new_pw = generator.generatePassword()

        site_dict[username] = {}
        site_dict[username]['password'] = new_pw
        site_dict[username]['past_pwds'] = [] if pw_curr == None else [pw_curr]
        site_dict[username]['params'] = params

        self.__writeEncryptedData(self.__data / site_cleaned, json.dumps(site_dict))
        return 'Account added'

    def newPassword(self, site, username):
        site_dict, userExists, site_cleaned = self.__loadSiteDictionary(site, username)
        if not userExists:
            return f'No account using {username} for {site} exists'

        generator = pg(site_dict[username]['params'])
        new_pw = generator.generatePassword()
        site_dict[username]['past_pwds'].append(site_dict[username]['password'])
        site_dict[username]['password'] = new_pw

        self.__writeEncryptedData(self.__data / site_cleaned, json.dumps(site_dict))
        return 'Password updated'

    def newParams(self, site, username, params):
        site_dict, userExists, site_cleaned = self.__loadSiteDictionary(site, username)
        if not userExists:
            return f'No account using {username} for {site} exists'

        site_dict[username]['params'] = params
        generator = pg(params)
        new_pw = generator.generatePassword()
        site_dict[username]['past_pwds'].append(site_dict[username]['password'])
        site_dict[username]['password'] = new_pw

        self.__writeEncryptedData(self.__data / site_cleaned, json.dumps(site_dict))
        return 'Params updated'
