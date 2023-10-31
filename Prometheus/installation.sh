docker pull prom/prometheus
docker run -d -p 9090:9090 --name=prometheus prom/prometheus


docker run \
    -p 9090:9090 \
    -v /path/to/prometheus.yml:/etc/prometheus/prometheus.yml \
    prom/prometheus
