#!/bin/bash

printf "\033[92mThis generates a new KeyLocker user.\033[0m\n"
read -p "Username: " username

sudo useradd $username -m -G kl_user
sudo passwd $username

printf "\033[93m[INFO]\033[0m Setting up basic user directory structure and files.\n"
sudo rsync -Larvtg /home/pi/KeyLocker/userdir/. /home/$username/.

printf "\033[93m[INFO]\033[0m Setting groups to protect configs and data directories.\n"
sudo chgrp $username /home/$username/configs
sudo chgrp $username /home/$username/data

printf "\033[93m[INFO]\033[0m The user \033[92m$username\033[0m has been successfully created.\n"
printf "\033[93m[INFO]\033[0m Useful scripts such as password change are located in the /home/$username/scripts/ directory.\n"

