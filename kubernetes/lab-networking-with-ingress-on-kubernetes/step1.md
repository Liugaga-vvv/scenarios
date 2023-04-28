# Install the Nginx Ingress Controller

First, we need to install the `nginx-ingress` controller in our cluster. We can do this by creating a Deployment and a Service that will be responsible for running the Ingress controller.

Create a namespace for the Ingress controller:

```
kubectl create namespace ingress-nginx
```

Install the `ingress-nginx` chart using `kubectl`:

```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.7.0/deploy/static/provider/cloud/deploy.yaml
```

Verify that the `ingress-nginx` controller pods are running:

```
kubectl get pods -n ingress-nginx
```
