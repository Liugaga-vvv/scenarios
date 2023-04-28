# Update an Existing Annotation

In this step, we will learn how to update an existing annotation on a Pod using the `kubectl annotate` command.

1. Use the `kubectl annotate` command to update the value of an existing annotation on the Pod:

```bash
kubectl annotate pod my-pod my-annotation-key-1=new-value --overwrite=true
```

2. Verify that the annotation has been updated on the Pod:

```bash
kubectl describe pod my-pod | grep my-annotation-key-1
```

You should see the updated value of `my-annotation-key-1` in the output.
