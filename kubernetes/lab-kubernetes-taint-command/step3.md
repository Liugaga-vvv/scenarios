# Modify a Taint on a Node

In this step, you will learn how to modify a taint on a node using the `kubectl taint` command. This can be useful if you need to update the restrictions or requirements of a node, but want to retain the existing taint key and effect.

1. Add a new taint with the following content:

```bash
kubectl taint nodes minikube app=uat:NoSchedule
```

2. Use overwrite to force updates

```bash
kubectl taint nodes minikube app=dev:NoSchedule --overwrite=true
```

It will update the `app` taint value from `prod` to `dev` on the `minikube` node. This will update the taint on the node while retaining the same taint key and effect.
