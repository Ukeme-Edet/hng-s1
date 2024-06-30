#!/usr/bin/bash
# This script is used to setup the environment for the project

# Install python3, python3-pip, python3-venv, python3-dev
sudo apt-get update -y
sudo apt-get install -y python3-pip python3-venv python3-dev nginx
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the required packages
pip install -r requirements.txt

# Create the service configuration file
sudo cp simple-service.service /etc/systemd/system/simple-service.service

# Reload the systemd manager configuration
sudo systemctl daemon-reload

# Start the service
sudo systemctl start simple-service

# Enable the service to start on boot
sudo systemctl enable simple-service

# Configure the nginx server
sudo cp simple-service /etc/nginx/sites-available/simple-service
sudo ln -sf /etc/nginx/sites-available/simple-service /etc/nginx/sites-enabled/simple-service
sudo systemctl restart nginx

# Change the permissions of the home directory
sudo chmod 755 /home/tech-wiz
