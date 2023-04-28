# Expose the Web Application

In this step, you will expose the web application to the outside world using a Kubernetes Service.

Create a file called `web-app-service.yaml` with the following contents:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-app
  namespace: webapp
spec:
  selector:
    app: web-app
  ports:
    - name: http
      port: 80
      targetPort: 80
  type: ClusterIP
```

This file creates a Service that exposes the web application to the cluster using a ClusterIP.

Apply the Service to your cluster with the following command:

```shell
kubectl apply -f web-app-service.yaml
```

Verify that the Service is running in the `webapp` namespace with the following command:

```shell
kubectl get services -n webapp
```

You should see the `web-app` service in the list of services running in the `webapp` namespace.
