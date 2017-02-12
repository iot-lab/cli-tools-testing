#!/bin/bash -ev

cat /dev/zero | ssh-keygen -q -N ""
./tests/install_ssh_key.py
cat > ~/.ssh/config <<EOF
Host *.iot-lab.info
User $IOTLAB_USER
EOF
#ssh grenoble.iot-lab.info -o StrictHostKeyChecking=no id
