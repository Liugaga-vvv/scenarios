# Cordon and Uncordon a Node

In some cases, you may need to take a node out of rotation for maintenance or other reasons. Kubernetes provides a way to mark a node as unschedulable so that no new pods are scheduled on it. This is called "cordon".

To cordon a node, use the following command:

```bash
kubectl cordon minikube
```

Replace `minikube` with the name of the node you want to cordon.

Then Use the following command to check the node status:

```bash
kubectl get node
```

To uncordon a node and allow new pods to be scheduled on it, use the following command:

```bash
kubectl uncordon minikube
```

Replace `minikube` with the name of the node you want to uncordon.

Note that cordoning a node does not automatically move any existing pods off the node. You should manually delete or move the pods before cordoning the node to avoid any disruption.

Congratulations, you have learned how to cordon and uncordon a node in Kubernetes.
