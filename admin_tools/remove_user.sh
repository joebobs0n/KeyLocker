#!/bin/bash

printf "\033[91mThis will remove the given user and ALL accompanying data (including encrypted password data).\033[0m\nAre you sure you wish to continue? (y/n): "
read confirm

if [ $confirm == "y" ]; then
    read -p "Username: " username

    printf "\033[93m[INFO]\033[0m Removing user $username.\n"
    sudo userdel --remove $username

    printf "\033[93m[INFO]\033[0m Removing /home/$username directory.\n"
    sudo rm -rf /home/$username

    printf "\033[93m[INFO]\033[0m The user \033[91m$username\033[0m has been successfully removed.\n"
fi

