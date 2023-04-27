# Verifying Cross-Namaspace Access

First, find the name of the pod running your application by running the following command:

```shell
kubectl get pods -l app=other
```

You should see the `other` pod. Note the name of the pod.

Next, run the following command to open a shell session in the container running your application:

```shell
kubectl exec -it sh < pod-name > --
```

Replace <pod-name> with the name of the pod that you noted earlier.

Once you are in the shell session, run the following command to access the `web-app` Deployment:

```shell
curl web-app.webapp
```

You should see the HTML response from the Nginx web server.
