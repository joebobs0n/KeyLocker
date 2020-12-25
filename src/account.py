#!/usr/bin/env python3

import xml.etree.ElementTree as et
import re


class Account():
    def __init__(self, site, usr, pw, params):
        self.__site = ''
        self.site = site

        self.__username = ''
        self.username = usr

        self.__password = ''
        self.password = pw

        self.__params = {}
        self.params = params

    @property
    def site(self):
        pass

    @site.setter
    def site(self, site):
        possible_tld = ''
        site_cleaned = site

        tld_file_path = '../bin/tld.txt' if __name__ == '__main__' else 'bin/tld.txt'
        with open(tld_file_path) as f:
            possible_tld = f.read()
        possible_tld = re.split('\n|\ ', possible_tld)
        possible_tld = [tld for tld in possible_tld if tld != '']
        possible_tld = '|'.join(possible_tld)

        http_found = re.finditer(f'^http(s)?://(www\.)?', site)
        for remove in http_found:
            site_cleaned = site_cleaned.replace(remove[0], '')

        tld_found = re.finditer(f'\.({possible_tld}).*', site)
        for remove in tld_found:
            site_cleaned = site_cleaned.replace(remove[0], '')
        site_cleaned = site_cleaned.lower()

        self.__site = site_cleaned

    @property
    def username(self):
        pass

    @username.setter
    def username(self, usr):
        self.__username = usr

    @property
    def password(self):
        pass

    @password.setter
    def password(self, pw):
        if pw == self.__password:
            raise ValueError('Repeat password')
        self.__password = pw

    @property
    def params(self):
        pass

    @params.setter
    def params(self, params):
        self.__params = params

    def toXML(self):
        element = et.Element('account')
        element.set('site', self.__site)
        element.set('username', self.__username)
        element.set('password', self.__password)
        element.set('params', self.__params)

        return element


if __name__ == '__main__':
    import os, sys
    os.chdir(sys.path[0])

    print('Initializing Account \'foo\'...')
    foo = Account('https://my.byu.edu', 'account_name@somewhere.com', 'th1s!s4dum|3pas5w0rd\'.',
    {
        'passLength': 20,
        'upper': True,
        'numeric': True,
        'punct': True,
        'other': '',
        'illegal': ''
    })

    print('Initializing Account \'bar\'...')
    bar = Account('https://www.youtube.com/watch?v=G1IbRujko-A&t', 'generic_username', 'badddp4ssword',
    {
        'passLength': 8,
        'upper': True,
        'numeric': True,
        'punct': False,
        'other': '',
        'illegal': 'ABCDEFGHIJKLMNOPQRSTUVWXY012345678'
    })

    print('\nTry to assign same password that is already set in \'foo\':')
    try:
        foo.password = 'th1s!s4dum|3pas5w0rd\'.'
    except:
        print(f'{sys.exc_info()}')


    x = foo.toXML()
    y = bar.toXML()

    print(f'\n\'foo\' account:\n    tag: {x.tag}\n    attrib: {x.attrib}')
    print(f'\'bar\' account:\n    tag: {y.tag}\n    attrib: {y.attrib}')
