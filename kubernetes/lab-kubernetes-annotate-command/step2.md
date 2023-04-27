# Annotate a Pod With Multiple Key-Value Pairs

In this step, we will explore how to add multiple annotations to a Pod using the `kubectl annotate` command.

1. Use the `kubectl annotate` command to add multiple annotations to the Pod:

```bash
kubectl annotate pod my-pod my-annotation-key-1=my-annotation-value-1 my-annotation-key-2=my-annotation-value-2
```

2. Verify that the annotations have been added to the Pod:

```bash
kubectl describe pod my-pod | grep my-annotation-key
```

You should see both annotations `my-annotation-key-1` and `my-annotation-key-2` with their corresponding values in the output.
