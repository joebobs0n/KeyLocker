#!/usr/bin/env python3

import xml.etree.ElementTree as et
import sys


class Account():
    def __init__(self, usr, pw):
        self.__username = ''
        self.username = usr

        self.__password = ''
        self.password = pw

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, usr):
        self.__username = usr

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, pw):
        if pw == self.__password:
            raise ValueError
        self.__password = pw

    def toXML(self):
        element = et.Element('account')
        element.set('username', self.username)
        element.set('password', self.password)

        return element


if __name__ == '__main__':
    foo = Account('account_name@somewhere.com', 'th1s!s4dum|3pas5w0rd\'.')
    bar = Account('generic_username', 'badddp4ssword')

    try:
        foo.password = 'th1s!s4dum|3pas5w0rd\'.'
    except:
        print(sys.exc_info())

    x = foo.toXML()
    y = bar.toXML()

    print(x.tag, x.attrib)
    print(y.tag, y.attrib)
