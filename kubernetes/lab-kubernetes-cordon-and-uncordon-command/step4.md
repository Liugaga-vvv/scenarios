# Using Labels to Cordon and Uncordon Nodes

In this step, we will use labels to cordoned and uncordoned nodes based on specific criteria. Here are the steps:

1. Label the nodes in the cluster using the following command:

```bash
kubectl label nodes minikube org=labex
```

2. Cordon the nodes that have the specified label using the following command:

```bash
kubectl cordon -l org=labex
```

3. Verify that the nodes have been cordoned by checking the `SchedulingDisabled` field in the nodes' status using the following command:

```bash
kubectl get node -l org=labex | grep SchedulingDisabled
```

4. Uncordon the nodes that have the specified label using the following command:

```bash
kubectl uncordon -l org=labex
```

5. Verify that the nodes have been uncordoned by checking the `SchedulingDisabled` field in the nodes' status using the following command:

```bash
kubectl get node -l org=labex | grep SchedulingDisabled
```
