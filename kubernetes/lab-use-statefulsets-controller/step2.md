# Create a StatefulSet

Create a file named `statefulset.yaml` with the following contents:

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
          image: nginx:1.19.7
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

In this file, we define a StatefulSet named `web` that creates three replicas of an NGINX pod. We also define a service named `web` that selects the NGINX pods using the `app: nginx` label. Finally, we define a persistent volume claim template for the NGINX pod's data.

To create the StatefulSet, run the following command:

```shell
kubectl apply -f statefulset.yaml
```

You can check the status of the StatefulSet by running the following command:

```shell
kubectl get statefulsets
```

Once the StatefulSet is running, you can access the NGINX pods by running the following command:

```shell
kubectl get pods
kubectl exec -it web-0 -- /bin/bash
```

Replace `web-0` with the name of any NGINX pod created by the StatefulSet.

Congratulations, you have successfully created a StatefulSet in Kubernetes!
