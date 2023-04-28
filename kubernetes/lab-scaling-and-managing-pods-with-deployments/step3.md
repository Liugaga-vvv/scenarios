# Update the Deployment

1. Edit the `my-deployment` Deployment to use the `nginx:1.19` image:

```bash
kubectl edit deployment my-deployment
```

This will open the Deployment in your default text editor. Change the `image` field to `nginx:1.19` and save the file.

2. Verify that the Deployment has been updated:

```bash
kubectl rollout status deployment/my-deployment
```

This will show you the status of the latest rollout of the `my-deployment` Deployment.
