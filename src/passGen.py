#!/bin/usr/env python3

import string
import numpy as np


class PasswordGenerator():
    def __init__(self, params):
        self.valid_chars = []
        self.symbols = []
        self.__setup(params['passLength'], params['upper'], params['numeric'], params['punct'], params['other'], params['illegal'])

    def __setup(self, passLength, upper, numeric, punct, other, illegal):
        self.length = passLength
        self.needUpper = upper
        self.needNumeric = numeric
        self.needSymbol = bool(punct or other)
        self.illegals = list(illegal)

        self.__setupValidChars(punct, other)

        if self.length < 8:
            raise ValueError("Password length must be 8 or greater.")
        if self.needUpper and (len(self.valid_uppercase) == 0):
            raise ValueError("No valid uppercase", f'Desired uppercase: {list(string.ascii_uppercase)}', f'Illegal: {illegal}')
        if self.needNumeric and (len(self.valid_digits) == 0):
            raise ValueError("No valid digits", f'Desired digits: {list(string.digits)}', f'Illegal: {illegal}')
        if self.needSymbol and (len(self.valid_symbols) == 0):
            desiredSymbols = set(string.punctuation) if punct else []
            desiredSymbols.union(list(other))
            raise ValueError("No valid symbols", f'Desired symbols: {list(desiredSymbols)}', f'Illegal: {illegal}')

    def __setupValidChars(self, punct, other):
        self.valid_lowercase = list(set(string.ascii_lowercase).difference(self.illegals))
        self.valid_uppercase = list(set(string.ascii_uppercase).difference(self.illegals))
        self.valid_digits = list(set(string.digits).difference(self.illegals))
        self.valid_symbols = set({})
        if punct:
            self.valid_symbols = self.valid_symbols.union(set(string.punctuation))
        if other:
            self.valid_symbols = self.valid_symbols.union(other)
        self.valid_symbols = list(self.valid_symbols.difference(self.illegals))

        self.valid_chars = self.valid_lowercase + self.valid_uppercase + self.valid_digits + self.valid_symbols

    def __checkHasNecessary(self, password):
        hasUpper = False if self.needUpper else True
        hasNumeric = False if self.needNumeric else True
        hasSymbol = False if self.needSymbol else True

        for char in password:
            if char in self.valid_uppercase:
                hasUpper = True
            elif char in self.valid_digits:
                hasNumeric = True
            elif char in self.valid_symbols:
                hasSymbol = True

        return hasUpper, hasNumeric, hasSymbol

    def __fixPassword(self, password, hasUpper, hasNumeric, hasSymbol):
        idx = []
        while len(idx) != 3:
            idx.append(np.random.randint(self.length))
            idx = list(set(idx))

        if not hasUpper:
            upperChar_idx = np.random.randint(len(self.valid_uppercase))
            password[idx[0]] = self.valid_uppercase[upperChar_idx]
        if not hasNumeric:
            numeric_idx = np.random.randint(len(self.valid_digits))
            password[idx[1]] = self.valid_digits[numeric_idx]
        if not hasSymbol:
            symbol_idx = np.random.randint(len(self.valid_symbols))
            password[idx[2]] = self.valid_symbols[symbol_idx]

        return password

    def generatePassword(self):
        pass_temp = []
        for i in range(self.length):
            thisChar = self.valid_chars[np.random.randint(len(self.valid_chars))]
            pass_temp.extend(thisChar)

        hasUpper, hasNumeric, hasSymbol = self.__checkHasNecessary(pass_temp)
        if not (hasUpper and hasNumeric and hasSymbol):
            pass_temp = self.__fixPassword(pass_temp, hasUpper, hasNumeric, hasSymbol)

        return ''.join(pass_temp)
