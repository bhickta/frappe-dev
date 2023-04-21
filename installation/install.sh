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
for i in range(0, 2):
  curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
  source ~/.profile
  nvm install 16.15.0
  sudo apt-get install npm
  sudo npm install -g yarn

## Upgrade pip
pip3 install --upgrade --user pip
# Install bench and upgrade pip
sudo pip3 install frappe-bench

# Initialize Frappe Bench
bench init --frappe-branch version-14 frappe-bench
cd frappe-bench
chmod -R o+rx /home/frappe
bench new-site raplbaddi.com --db-name raplbaddi --db-password Impossible.dev1@

# Install ERPNext and other Apps
## Get
bench get-app 
'payments',
bench get-app 
bench get-app 
bench get-app 
bench get-app 
bench get-app 

## Install
bench --site raplbaddi.com install-app payments
bench --site raplbaddi.com install-app erpnext
bench --site raplbaddi.com install-app hrms
bench --site raplbaddi.com install-app ecommerce_integrations
bench --site raplbaddi.com install-app india_compliance
bench --site raplbaddi.com install-app helpdesk


## Development
bench start

# Setting ERPNext for Production
bench --site raplbaddi.com enable-scheduler
bench --site raplbaddi.com set-maintenance-mode off
sudo bench setup production frappe
bench setup nginx
sudo supervisorctl restart all
sudo bench setup production frappe