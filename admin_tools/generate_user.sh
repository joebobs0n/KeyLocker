#!/bin/bash

read -p 'Username: ' username

sudo useradd $username -m -G kl_user -s $(which fish)
sudo passwd $username

#sudo cp -Rp --attributes-only /home/pi/KeyLocker/userdir/* /home/$username/.
sudo rsync -Larvtg /home/pi/KeyLocker/userdir/. /home/$username/.

sudo chgrp $username /home/$username -R
