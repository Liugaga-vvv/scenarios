# Deploy a Simple Web Application

In this step, you will deploy a simple web application that will store data on the PersistentVolume you created in Step 1. You will create a YAML file called `web-app.yaml` with the following content:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
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
        - name: web-app
          image: nginx
          volumeMounts:
            - name: data
              mountPath: /usr/share/nginx/html/data
      volumes:
        - name: data
          persistentVolumeClaim:
            claimName: my-pvc
```

This file creates a Deployment with one replica and a container that runs the nginx image. The `volumeMounts` field specifies that the container should mount the PersistentVolume at the path `/usr/share/nginx/html/data`. The `volumes` field specifies that the container should use a PersistentVolumeClaim called `my-pvc`.

Apply the Deployment to your cluster with the following command:

```shell
kubectl apply -f web-app.yaml
```
