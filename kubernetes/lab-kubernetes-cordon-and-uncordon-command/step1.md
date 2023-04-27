# Cordoning a Node

In this step, we will use the `cordon` command to mark a node as "unschedulable", preventing new pods from being scheduled on that node. Here are the steps:

1. List the nodes in the cluster using the following command:

```bash
kubectl get nodes
```

2. Cordon the node using the following command:

```bash
kubectl cordon minikube
```

3. Verify that the node has been cordoned by checking the `SchedulingDisabled` field in the node's status using the following command:

```bash
kubectl get node | grep SchedulingDisabled
```
