#!/bin/bash -ev

cat /dev/zero | ssh-keygen -q -N ""
./tests/install_ssh_key.py
#ssh $IOTLAB_USER@grenoble.iot-lab.info -o StrictHostKeyChecking=no id
