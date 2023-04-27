# Deploy a Web Application

In this step, you will deploy a simple web application in the `webapp` namespace.

Create a file called `web-app.yaml` with the following contents:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
  namespace: webapp
spec:
  replicas: 1
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: web-app
    spec:
      containers:
        - name: nginx
          image: nginx:latest
          ports:
            - containerPort: 80
```

This file creates a Deployment with one replica of a container that runs the latest version of the Nginx web server.

Apply the Deployment to your cluster with the following command:

```shell
kubectl apply -f web-app.yaml
```

Verify that the web application is running in the `webapp` namespace with the following command:

```shell
kubectl get pods -n webapp
```

You should see the `web-app` pod in the list of pods running in the `webapp` namespace.
