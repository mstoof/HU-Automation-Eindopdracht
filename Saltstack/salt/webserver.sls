install_docker:
  pkg.installed:
    - names:
      - docker
      - docker-compose

enable_docker_service:
  service.running:
    - name: docker
    - enable: True
    - require:
      - pkg: install_docker
