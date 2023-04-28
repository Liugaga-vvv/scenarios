# Create an Ingress Resource

Now that we have the Ingress controller set up and a backend service running, we can create the rules for the Ingress resource.

In this example, we will create a simple rule to route traffic for the `example.com` domain to our backend service:

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: test-ingress
  annotations:
    kubernetes.io/ingress.class: nginx
spec:
  rules:
  - host: example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: sample-app
            port:
              name: http
```

The YAML file called `ingress.yaml`. Apply the Ingress resource to the cluster:

```
kubectl apply -f ingress.yaml
```
