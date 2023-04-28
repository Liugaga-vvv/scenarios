# Update a StatefulSet

In Kubernetes, you can update a StatefulSet's pods by updating its template. Let's update the `statefulset.yaml` file to use NGINX version 1.20.0.

Update the `statefulset.yaml` file to the following:

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: web
spec:
  serviceName: "web"
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:1.20.0
          ports:
            - containerPort: 80
          volumeMounts:
            - name: www
              mountPath: /usr/share/nginx/html
  volumeClaimTemplates:
    - metadata:
        name: www
      spec:
        accessModes: ["ReadWriteOnce"]
        resources:
          requests:
            storage: 1Gi
```

To update the StatefulSet, run the following command:

```shell
kubectl apply -f statefulset.yaml
```

You can check the status of the StatefulSet by running the following command:

```shell
kubectl get statefulsets
```

Congratulations, you have successfully updated a StatefulSet in Kubernetes!
