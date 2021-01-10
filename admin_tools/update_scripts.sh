#!/bin/bash

for dir in /home/*
do
    if [ $dir != '/home/pi' ]
        then
        sudo rm -rf $dir/scripts/*
        sudo cp -Rp /home/pi/KeyLocker/userdir/scripts/. $dir/scripts/.
    fi
done

