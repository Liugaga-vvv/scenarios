# Create a Deployment

1. Create a file called `my-deployment.yaml` in `/home/labex/project/` with the following content::

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
        - name: my-app
          image: nginx:latest
          ports:
            - containerPort: 80
```

This YAML file defines a Deployment with 3 replicas, running an Nginx container. The `selector` field selects the Pods controlled by the Deployment based on the `app` label.

2. Deploy the `my-deployment` Deployment:

```bash
kubectl apply -f my-deployment.yaml
```

This will create the `my-deployment` Deployment and its associated ReplicaSets and Pods.

3. Verify that the Deployment has been created:

```bash
kubectl get deployments
```

This will show you the Deployments in your cluster, including the `my-deployment` Deployment.
