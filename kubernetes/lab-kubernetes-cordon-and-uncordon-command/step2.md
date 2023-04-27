# Uncordoning a Node

In this step, we will use the `uncordon` command to mark a node as "schedulable" again, allowing new pods to be scheduled on that node. Here are the steps:

1. Uncordon the node using the following command:

```bash
kubectl uncordon minikube
```

2. Verify that the node has been uncordoned by checking the `SchedulingDisabled` field in the node's status using the following command:

```bash
kubectl get node | grep SchedulingDisabled
```
