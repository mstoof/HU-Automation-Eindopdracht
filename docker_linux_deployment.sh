#!/bin/bash

# Update the system's package repository
sudo apt-get update && sudo apt-get upgrade -y

# Install Docker
sudo apt-get install -y docker.io

# Start Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Pull and run a Docker container (example with a web server)
sudo docker pull nginx
sudo docker run -d -p 80:80 --name webserver nginx
