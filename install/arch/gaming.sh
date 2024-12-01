#!/bin/bash

sudo systemctl enable cpupower.service
sudo systemctl start cpupower.service

# Set CPU governor to performance
echo "Setting CPU governor to performance..."
sudo cpupower frequency-set -g performance

# Verify CPU governor setting
echo "Current CPU governor:"
cpupower frequency-info | grep "The governor"

echo "Service started and CPU set to performance mode."

sudo grub-mkconfig -o /boot/grub/grub.cfg

sudo systemctl enable tlp
sudo systemctl enable fstrim.timer
