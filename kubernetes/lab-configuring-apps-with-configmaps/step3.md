# Verify the Configuration

In this step, you will verify that the configuration has been applied to your application.

First, find the name of the pod running your application by running the following command:

```bash
kubectl get pods -l app=my-app
```

You should see a single pod running your application. Note the name of the pod.

Next, run the following command to open a shell session in the container running your application:

```bash
kubectl exec -it sh < pod-name > --
```

Replace `<pod-name>` with the name of the pod that you noted earlier.

Once you are in the shell session, run the following command to print the value of the `DATABASE_URL` environment variable:

```bash
echo $DATABASE_URL
```

You should see the database connection string that you set in the ConfigMap.
