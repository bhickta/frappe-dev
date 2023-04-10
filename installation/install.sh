#!/bin/bash

# Load environment variables from .env file
source .env

# Install prerequisites
## Database and Redis-server
sudo apt-get install -y mariadb-server mariadb-client redis-server
## Supervisor
sudo apt install -y supervisor
## Git and Curl
sudo apt-get install -y curl git
## Python
sudo apt-get install -y python3-dev python3.10-dev python3-setuptools python3-pip python3-distutils python3.10-venv software-properties-common
## Miscellaneous
sudo apt-get install -y xvfb libfontconfig wkhtmltopdf libmysqlclient-dev


## Configure mysql server
echo -e "y\n$your_current_root_password\n$your_desired_root_password\ny\ny\ny\ny" | sudo mysql_secure_installation

# Restart the Mysql Server
sudo service mysql restart

# Install nvm, npm and yarn
curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
source ~/.profile
nvm install lts
sudo apt-get install npm
sudo npm install -g yarn

# Install bench
sudo pip3 install frappe-bench

# Initialize Frappe Bench
bench init --frappe-branch version-14 frappe-bench
cd frappe-bench
chmod -R o+rx /home/$frappe_user
bench new-site $site_name

# Install ERPNext and other Apps
## Get
bench get-app payments
bench get-app --branch version-14 erpnext
bench get-app hrms
## Install
bench --site $site_name install-app erpnext
bench --site $site_name install-app hrms

# Setting ERPNext for Production
bench --site $site_name enable-scheduler
bench --site $site_name set-maintenance-mode off
sudo bench setup production $frappe_user
bench setup nginx
sudo supervisorctl restart all
sudo bench setup production $frappe_user
