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
    - [ ] touchscreen display for menus and traversal
      - [the one i have (have to upload image bins to board and then use internal command to manipulate)](https://www.ebay.com/itm/New-3-5-HMI-I2C-LCD-Display-Module-Capacitive-Touch-Screen-480x320-for-Arduino/264732561635?hash=item3da34a50e3:g:CNsAAOSw6rVev6aR) - [documentation](https://www.adrive.com/public/gtyuYs/0128058%202.8%203.5%204.3%205inch%20display%20%20i2c_package_english_v1.2.zip)
      - [cheap alternative option with case specifically for raspberry pi through GPIO (need drivers)](https://www.ebay.com/itm/3-5-Touch-Screen-Display-320-480-With-Case-Touch-Pen-For-Raspberry-Pi-4-US/114412139853?_trkparms=aid%3D1110006%26algo%3DHOMESPLICE.SIM%26ao%3D1%26asc%3D225085%26meid%3D43a208f7edd14cfe9e7ba529be644731%26pid%3D100005%26rk%3D4%26rkt%3D12%26mehot%3Dco%26sd%3D362836286867%26itm%3D114412139853%26pmt%3D1%26noa%3D1%26pg%3D2047675%26algv%3DSimPromoteOrganicWithFloorBidWebWithBBEV2%26brand%3DUnbranded&_trksid=p2047675.c100005.m1851)
      - [slightly less cheap option with acrylic case specifically for raspberry pi through HDMI jack](https://www.amazon.com/Miuzei-Raspberry-Full-Angle-Heatsinks-Raspbian/dp/B07XBVF1C9/ref=sr_1_3?dchild=1&keywords=3.5%22+raspberry+pi+4+touchscreen&qid=1609104965&refinements=p_85%3A2470955011&rnid=2470954011&rps=1&sr=8-3)

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
  - additional domains can be added (i.e. com, org, edu ...)
- [x] `bin/params_db.json` exists for user add/use password parameter profiles