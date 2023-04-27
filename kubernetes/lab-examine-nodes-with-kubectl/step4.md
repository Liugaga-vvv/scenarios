# View Node Capacity and Resource Usage

To view the available resources on a node, use the following command:

```
kubectl describe node minikube | grep -A 8 "Allocated resources"
```

Replace `minikube` with the name of the node you want to examine.

This will provide detailed information about the node, including its capacity and current resource usage.
