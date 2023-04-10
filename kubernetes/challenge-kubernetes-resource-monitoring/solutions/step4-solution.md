# Note

- Input `vim /home/labex/prometheus-service.yaml` command to add Prometheus service.
- Input `kubectl apply -f prometheus-service.yaml` command to create the service.
- Input `kubectl get svc -n monitoring` command to get the service's Nodeport.
- Input `kubectl get node -o wide` command to get the node IP.
