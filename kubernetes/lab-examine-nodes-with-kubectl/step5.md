# View Node Events

In Kubernetes, you can use the following command to filter all events related to a specific node:

```bash
kubectl get events --field-selector involvedObject.kind=Node,involvedObject.name=minikube
```

Replace `minikube` with the name of the node you want to query. This command will list all events related to that node, such as restarts, upgrades, and so on.
