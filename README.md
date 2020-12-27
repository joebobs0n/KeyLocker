# KeyLocker

## User Interfaces:
- [ ] **Commandline Interface (SSH)**
  - Functionality
    - [ ] add new account
    - [ ] generate new password
    - [ ] view sites/usernames (not passwords)
  - Operation
    - [ ] honeypot typical SSH ports (22, 2222, 8080, 1234)
    - [ ] allow user on first boot to choose *their* port for SSH access
      - [ ] afterward setup port becomes honeypot
      - [ ] user selected port has limited access
    - [ ] setup secret admin port with all access

- [ ] **Raspberry Pi Hat (MCU-like)**
  - Functionality
    - [ ] generate new password
    - [ ] view sites/usernames (likely through menus)
    - [ ] inject username to host machine
    - [ ] inject password to host machine
  - Operation
    - [ ] PCB hat on the raspberry pi
      - [ ] display for menus
      - [ ] rotary encoder for menu traversal

- [ ] **Apache 2.0 (localhost)**
  - Functionality
    - [ ] add new account
    - [ ] view sites/usernames (not passwords)
  - Operation
    - [ ] Wyatt

</br>

## Backend Operation/Functionality:
- [x] `locker.py`
  - [x] `__init__(self)`
  - [x] `access(self, site)`
  - [x] `add(self, site, username, params=None, pw_curr=None)`
  - [x] `newPassword(self, site, username)`
  - [x] `newParams(self, site, username, params)`
- [x] `passGen.py`
  - [x] `__init__(self, params)`
  - [x] `generatePassword(self)`

</br>

## Features:
- [x] on first run, encryption key generated automatically and saved
  - [ ] perhaps create backup of encryption key that can't be deleted and reloaded in case of working key loss
- [x] if `bin/tld` file missing, minimal one is generated and saved
  - used to clean inputs and file management
  - can be added to for additional domains (i.e. com, org, edu ...)
- [x] `bin/params_db.json` exists for user add/use password parameter profiles