# For Ubuntu/Debian systems
sudo apt update
sudo apt install docker.io

# For CentOS/RHEL systems
sudo yum install docker

sudo systemctl start docker
sudo systemctl enable docker  # To ensure Docker starts on boot

docker build -t my-nginx-image .

docker run --name my-nginx-container -d -p 80:80 my-nginx-image

docker-compose up