# /srv/salt/nginx.sls

install_nginx:
  pkg.installed:
    - name: nginx

nginx_service:
  service.running:
    - name: nginx
    - enable: True
    - watch:
      - pkg: install_nginx

include:
  - .nginx_config

nginx_service:
  service.running:
    - name: nginx
    - enable: True
    - require:
      - file: nginx_configuration

nginx_configuration:
  file.managed:
    - name: /etc/nginx/sites-available/default
    - source: salt://nginx/default.conf
    - template: jinja
    - context:
        config: {{ salt['pillar.get']('nginx:server_block_config') }}
    - watch_in:
      - service: nginx_service
