# Note

1. Create a file called `mysql.yaml` with the following content.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mysql
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
        - name: mysql
          image: mysql:5.7
          env:
            - name: MYSQL_ROOT_PASSWORD
              value: root
            - name: MYSQL_DATABASE
              value: hello-world
          ports:
            - containerPort: 3306
              name: mysql
          volumeMounts:
            - name: mysql-persistent-storage
              mountPath: /var/lib/mysql
      volumes:
        - name: mysql-persistent-storage
          emptyDir: {}
---
apiVersion: v1
kind: Service
metadata:
  name: mysql
spec:
  selector:
    app: mysql
  ports:
    - port: 3306
      targetPort: 3306
```

Then use the following command to create MySQL.

```bash
kubectl apply -f mysql.yaml
```

2.  Create a file called `hello-world.yaml` with the following content.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: helloworld
spec:
  replicas: 3
  selector:
    matchLabels:
      app: hello-world
  template:
    metadata:
      labels:
        app: hello-world
    spec:
      containers:
        - name: hello-world
          image: labex/go-hello-world:v2.0
          env:
            - name: MYSQL_USER
              value: root
            - name: MYSQL_PASSWORD
              value: root
            - name: MYSQL_ADDRESS
              value: mysql
            - name: MYSQL_DBNAME
              value: hello-world
            - name: CONTENT
              value: Hello World
          ports:
            - containerPort: 8080
---
apiVersion: v1
kind: Service
metadata:
  name: helloworld
spec:
  selector:
    app: hello-world
  ports:
    - name: http
      port: 8080
      targetPort: 8080
      nodePort: 31323
  type: NodePort
```

Then use the following command to create the deployment.

```bash
kubectl apply -f hello-world.yaml
```

3. Use `kubectl get node -o wide` command to get the node IP.
4. Use `kubectl get service` command to get the `helloworld` service's NodePort.
