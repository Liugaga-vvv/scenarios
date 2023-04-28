# Test Access

Test access to create a pod in the `myapp` namespace by creating a pod using the following YAML file called `myapp-pod.yaml`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
  namespace: myapp
spec:
  containers:
    - name: myapp-container
      image: nginx
      ports:
        - containerPort: 80
```

Create the pod using the following command:

```shell
kubectl apply -f myapp-pod.yaml --as cluster-admin
```

You should see a message indicating that the pod was created.

Test access to create a deployment in the `myapp` namespace by creating a deployment using the following YAML file `myapp-deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-deployment
  namespace: myapp
spec:
  replicas: 1
  selector:
    matchLabels:
      app: myapp-deployment
  template:
    metadata:
      labels:
        app: myapp-deployment
    spec:
      containers:
        - name: nginx
          image: nginx:latest
          ports:
            - containerPort: 80
```

Create the pod using the following command:

```shell
kubectl apply -f myapp-deployment.yaml --as cluster-admin
```

You should see an error message indicating that you do not have access to create deploymeny in the `myapp` namespace.
