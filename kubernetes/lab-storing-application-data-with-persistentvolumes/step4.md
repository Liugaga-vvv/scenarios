# Verify Data Persistence

In this step, you will verify that the data is being persisted on the PersistentVolume. You will access the web application running on the container and write some data to the PersistentVolume.

First, find the name of the pod running your application by running the following command:

```shell
kubectl get pods -l app=web-app
```

You should see a single pod running your application. Note the name of the pod.

Next, run the following command to open a shell session in the container running your application:

```shell
kubectl exec -it sh < pod-name > --
```

Replace <pod-name> with the name of the pod that you noted earlier.

Once you are in the shell session, run the following command to add a test.txt file:

```shell
echo "This is a test file." > /usr/share/nginx/html/data/test.txt
```

This command creates a file called `test.txt` with the text "This is a test file." in the data directory of the PersistentVolume.

Delete the web application with the following command:

```shell
kubectl delete deployment web-app
```

Recreate the web application with the following command:

```shell
kubectl apply -f web-app.yaml
```

Verify that the file you created in the data directory still exists with the following command:

```shell
kubectl get pods -l app=web-app
kubectl exec cat /usr/share/nginx/html/data/test.txt < pod-name > --
```

Replace <pod-name> with the name of the pod that you noted earlier.
