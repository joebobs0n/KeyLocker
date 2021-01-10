#!/bin/bash

printf '\033[91mThis will remove the given user and ALL accompanying data (including encrypted password data).\nAre you sure you wish to continue? (y/n):\033[0m '
read confirm

if [ $confirm == 'y' ]; then
    read -p 'Username: ' username

    sudo userdel --remove $username
    sudo rm -rf /home/$username
fi

