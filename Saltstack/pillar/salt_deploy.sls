pull_flask_docker_image:
  cmd.run:
    - name: docker pull mstoof/aut-eindopdracht
    - require:
      - service: enable_docker_service

run_flask_docker_container:
  docker_container.running:
    - name: your-flask-app
    - image: username/your-flask-app
    - port_bindings: 80:5000  # Map TCP port 5000 in the container to port 80 on the Docker host
    - restart_policy: always
    - require:
      - cmd: pull_flask_docker_image
