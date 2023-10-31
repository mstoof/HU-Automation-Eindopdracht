# Start with the official Nginx image from Docker Hub
FROM nginx:latest

# Copy the website static files to the container
COPY ./Webserver /usr/share/nginx/html

# Expose port 80 to the outside world
EXPOSE 80

# Start Nginx when the container has provisioned.
CMD ["nginx", "-g", "daemon off;"]
