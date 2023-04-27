# Scale the Deployment

1. Scale up the `my-deployment` Deployment to 5 replicas:

```bash
kubectl scale deployment my-deployment --replicas=5
```

This will increase the number of replicas in the `my-deployment` Deployment to 5.

2. Verify that the Deployment has been scaled:

```bash
kubectl get deployments
```

This will show you the Deployments in your cluster, including the `my-deployment` Deployment with 5 replicas.
