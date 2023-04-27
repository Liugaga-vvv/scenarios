# Roll Back the Deployment

1. Roll back the `my-deployment` Deployment to the previous version:

```bash
kubectl rollout undo deployment/my-deployment
```

This will roll back the `my-deployment` Deployment to the previous version.

2. Verify that the Deployment has been rolled back:

```bash
kubectl rollout status deployment/my-deployment
```

This will show you the status of the latest rollout of the `my-deployment` Deployment.
