# Verify the Update

In this step, you will verify that the update to the ConfigMap has been applied to your application.

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

You can see that the configuration did not take effect, it is still the same data as before. You need to restart Deployment with the following command.

```bash
kubectl rollout restart deployment my-app
```

When the reboot is complete, go inside the container again and use the above command to check the configuration.

You should see the updated database connection string.
