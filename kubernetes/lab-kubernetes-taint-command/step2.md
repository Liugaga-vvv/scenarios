# Remove a Taint From a Node

In this step, you will learn how to remove a taint from a node using the `kubectl taint` command. This can be useful if you need to update the restrictions or requirements of a node, or if you want to allow pods to be scheduled on a previously tainted node.

To remove a taint from a node, you can use the following command:

```bash
kubectl taint nodes minikube app-
```

It will remove the `app=prod:NoSchedule` taint from the `minikube` node. This will allow pods to be scheduled on the node without needing to tolerate the previously applied taint.
