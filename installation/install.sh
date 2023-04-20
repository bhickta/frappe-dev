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
nvm install 16.15.0
sudo apt-get install npm
sudo npm install -g yarn

# Install bench and upgrade pip
sudo pip3 install frappe-bench
## Upgrade pip
pip3 install --upgrade --user pip

# Initialize Frappe Bench
bench init --frappe-branch version-14 frappe-bench
cd frappe-bench
chmod -R o+rx /home/frappe
bench new-site raplbaddi.com --db-name raplbaddi --db-password Impossible.dev1@

# Install ERPNext and other Apps
## Get
bench get-app payments
bench get-app --branch version-14 erpnext
bench get-app --branch version-14 hrms
bench get-app ecommerce_integrations
bench get-app --branch version-14 https://github.com/resilient-tech/india-compliance.git
bench get-app helpdesk

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

cp example.env ~/gitops/erpnext-raplbaddi.env
sed -i 's/DB_PASSWORD=123/DB_PASSWORD=Impossible.dev1@/g' ~/gitops/erpnext-raplbaddi.env
sed -i 's/DB_HOST=/DB_HOST=mariadb-database/g' ~/gitops/erpnext-raplbaddi.env
sed -i 's/DB_PORT=/DB_PORT=3306/g' ~/gitops/erpnext-raplbaddi.env
sed -i 's/SITES=`erp.example.com`/SITES=\`raplbadd.com\`, /g' ~/gitops/erpnext-raplbaddi.env
echo 'ROUTER=erpnext-raplbaddi' >> ~/gitops/erpnext-raplbaddi.env
echo "BENCH_NETWORK=erpnext-raplbaddi" >> ~/gitops/erpnext-raplbaddi.env

docker compose --project-name erpnext-raplbaddi \
  --env-file ~/gitops/erpnext-raplbaddi.env \
  -f compose.yaml \
  -f overrides/compose.redis.yaml \
  -f overrides/compose.multi-bench.yaml \
  -f overrides/compose.multi-bench-ssl.yaml config > ~/gitops/erpnext-raplbaddi.yaml

sudo  docker compose --project-name erpnext-raplbaddi -f ~/gitops/erpnext-raplbaddi.yaml up -d
# raplbaddi.com
sudo docker compose --project-name erpnext-raplbaddi exec backend \
  bench new-site raplbaddi.com --no-mariadb-socket --mariadb-root-password Impossible.dev1@ --install-app erpnext --admin-password Impossible.dev1@

echo "ROUTER=erpnext-raplbaddi" > ~/gitops/erpnext-raplbaddi.env
echo "SITES=\`raplbaddi.com\`" >> ~/gitops/erpnext-raplbaddi.env
echo "BASE_SITE=raplbaddi.com" >> ~/gitops/erpnext-raplbaddi.env
echo "BENCH_NETWORK=erpnext-raplbaddi" >> ~/gitops/erpnext-raplbaddi.env

docker compose --project-name erpnext-raplbaddi \
  --env-file ~/gitops/erpnext-raplbaddi.env \
  -f overrides/compose.custom-domain.yaml \
  -f overrides/compose.custom-domain-ssl.yaml config > ~/gitops/erpnext-raplbaddi.yaml

docker compose --project-name erpnext-raplbaddi -f ~/gitops/erpnext-raplbaddi.yaml up -d