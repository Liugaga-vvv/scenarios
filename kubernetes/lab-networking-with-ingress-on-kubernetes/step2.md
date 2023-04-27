# Create a Sample Application

Next, we will create a sample application that we will expose using Ingress.

Create a Deployment for a sample application:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: sample-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: sample-app
  template:
    metadata:
      labels:
        app: sample-app
    spec:
      containers:
      - name: sample-app
        image: nginx
        ports:
        - containerPort: 80
```

The YAML file called `sample-app.yaml`. Apply the deployment to your cluster with the following command:

```
kubectl apply -f sample-app.yaml
```

Create a Service for the sample application:

```
apiVersion: v1
kind: Service
metadata:
  name: sample-app
spec:
  selector:
    app: sample-app
  ports:
  - name: http
    port: 80
    targetPort: 80
```

The YAML file called `service-sample-app.yaml`. Apply the deployment to your cluster with the following command:

```
kubectl apply -f service-sample-app.yaml
```
