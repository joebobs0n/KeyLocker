#!/bin/bash

for dir in /home/*; do
    if [ $dir != '/home/pi' ]; then
        printf "\033[93m[info]\033[0m Updating $dir/scripts/\n"
        sudo rm -rf $dir/scripts/*
        sudo chgrp kl_user -R /home/pi/KeyLocker/userdir/scripts
        sudo chmod 750 -R /home/pi/KeyLocker/userdir/scripts
        sudo rsync -Larvtg /home/pi/KeyLocker/userdir/scripts/. $dir/scripts/.
    fi
done

