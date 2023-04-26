# Scale a StatefulSet

In Kubernetes, you can scale a StatefulSet up or down by changing its `replicas` field. Let's scale our `web` StatefulSet to five replicas.

Update the `statefulset.yaml` file to the following:

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: web
spec:
  serviceName: "web"
  replicas: 5
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

Congratulations, you have successfully scaled a StatefulSet in Kubernetes!
