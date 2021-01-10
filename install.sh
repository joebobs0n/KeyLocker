#!/bin/bash

sudo chmod 700 -R .
sudo chmod 770 -R userdir
sudo chmod 750 -R userdir/scripts

sudo chgrp kl_user -R userdir
