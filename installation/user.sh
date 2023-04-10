#!/bin/bash

# Load environment variables from .env file
source .env

# Update and Upgrade
sudo apt update -y
sudo apt upgrade -y

# Add user
sudo adduser $frappe_user
usermod -aG sudo $frappe_user
su $frappe_user
cd /home/$frappe_user