# Use the Configmap in Your Application

In this step, you will use the ConfigMap in your application.

Create a file named `deployment.yaml` in `/home/labex/project/` directory with the following contents:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 1
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
          env:
            - name: DATABASE_URL
              valueFrom:
                configMapKeyRef:
                  name: my-config
                  key: DATABASE_URL
```

This deployment specifies a single container running your application, which uses the `DATABASE_URL` environment variable to connect to a PostgreSQL database. The value of `DATABASE_URL` is obtained from the `my-config` ConfigMap.

To create the deployment, run the following command:

```bash
kubectl apply -f deployment.yaml
```
