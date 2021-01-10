#!/bin/bash

printf '\033[92mThis generates a new KeyLocker user.\033[0m\n'
read -p 'Username: ' username

sudo useradd $username -m -G kl_user
sudo passwd $username

#sudo cp -Rp --attributes-only /home/pi/KeyLocker/userdir/* /home/$username/.
sudo rsync -Larvtg /home/pi/KeyLocker/userdir/. /home/$username/.

sudo chgrp $username /home/$username/configs
sudo chgrp $username /home/$username/data
