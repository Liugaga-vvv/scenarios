# Verify Namespace Isolation

In this step, you will verify that the web application is isolated from the other resources in the cluster.

Create a file called `other-app.yaml` with the following contents:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: other
spec:
  replicas: 1
  selector:
    matchLabels:
      app: other
  template:
    metadata:
      labels:
        app: other
    spec:
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80
```

In this file, you are creating another Deployment called `other` in the default namespace that runs a container with the `nginx` image.

Apply the Deployment to your cluster with the following command:

```shell
kubectl apply -f other-app.yaml
```

Verify that the Deployment is running in the default namespace with the following command:

```shell
kubectl get pods | grep other
```

You should see the `other` pod in the list of pods running in the default namespace.
