# Add a Taint to a Node

In this step, you will learn how to add a taint to a node using the `kubectl taint` command. Taints are used to mark a node with certain restrictions or requirements, which can affect the scheduling of pods on that node.

To add a taint to a node, you can use the following command:

```bash
kubectl taint nodes minikube app=prod:NoSchedule
```

This will add a taint with key `app` and value `prod` to a node named `minikube`, with the effect `NoSchedule`. This will prevent pods from being scheduled on the node unless they tolerate the taint.

Then you can view the taints that are currently applied to nodes in your Kubernetes cluster using the `kubectl describe node` command.

To view the taints on a node, you can use the following command:

```bash
kubectl describe node minikube
```

The taints applied to the node will be listed under the "Taints" section in the output. You can use this information to verify that the taint you added in the previous step is applied to the node.
