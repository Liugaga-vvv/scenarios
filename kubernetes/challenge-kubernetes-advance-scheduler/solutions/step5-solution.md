# Note

1. Create a Kubernetes YAML file named `low-request-pod.yaml` with the following content:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: low-request-pod
spec:
  containers:
    - name: low-request-container
      image: nginx:latest
      resources:
        limits:
          cpu: "10m"
          memory: "100Mi"
        requests:
          cpu: "10m"
          memory: "100Mi"
```

Once you have created this YAML file, you can apply it to your Kubernetes cluster using the `kubectl` apply command.

```bash
kubectl apply -f low-request-pod.yaml
```

This will deploy one Pod with the specified resource requirements. You can observe if the Pod can be scheduled and started correctly by checking its status using the `kubectl get pods` command.

```bash
kubectl get pods
```

2. Create a Kubernetes YAML file named `high-request-pod.yaml` with the following content:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: high-request-pod
spec:
  containers:
    - name: high-request-container
      image: my-image:latest
      resources:
        limits:
          cpu: "3"
          memory: "4G"
        requests:
          cpu: "3"
          memory: "4G"
```

Once you have created this YAML file, you can apply it to your Kubernetes cluster using the `kubectl` apply command.

```bash
kubectl apply -f high-request-pod.yaml
```
