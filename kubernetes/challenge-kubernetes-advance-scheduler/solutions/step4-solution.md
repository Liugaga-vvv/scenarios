# Note

1. Input `kubectl apply -f high-priority.yaml` command to create a high priority to the cluster.
2. Input `kubectl apply -f low-priority.yaml` command to create a low priority to the cluster.
3. Create a Kubernetes YAML file named `low-priority-pods.yaml` with the following content:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: low-priority-pods
spec:
  replicas: 20
  selector:
    matchLabels:
      app: low-priority-pods
  template:
    metadata:
      labels:
        app: low-priority-pods
    spec:
      priorityClassName: low-priority
      containers:
        - name: low-priority-container
          image: nginx:latest
          resources:
            limits:
              cpu: "500m"
              memory: "256Mi"
            requests:
              cpu: "500m"
              memory: "256Mi"
```

Once you have created this YAML file, you can apply it to your Kubernetes cluster using the `kubectl` apply command.

```bash
kubectl apply -f low-priority-pods.yaml
```

4. Create a Kubernetes YAML file named `high-priority-pods.yaml` with the following content:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: high-priority-pods
spec:
  replicas: 1
  selector:
    matchLabels:
      app: high-priority-pods
  template:
    metadata:
      labels:
        app: high-priority-pods
    spec:
      priorityClassName: high-priority
      containers:
        - name: high-priority-container
          image: nginx:latest
          resources:
            limits:
              cpu: "1000m"
              memory: "256Mi"
            requests:
              cpu: "1000m"
              memory: "256Mi"
```

Once you have created this YAML file, you can apply it to your Kubernetes cluster using the `kubectl` apply command.

```bash
kubectl apply -f high-priority-pods.yaml
```
