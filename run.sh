#!/usr/bin/bash
# This script is used to run the project

# Check if the env file exists
if [ ! -f ".env" ]; then
	echo "The .env file does not exist. Please create the .env file and try again."
	exit 1
fi

# This script is used to run the project
sudo systemctl restart nginx

# Start the service
sudo systemctl start simple-service
