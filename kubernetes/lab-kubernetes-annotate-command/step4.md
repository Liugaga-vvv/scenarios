# Remove an Annotation

In this step, we will see how to remove an annotation from a Pod using the `kubectl annotate` command.

1. Use the `kubectl annotate` command with the `--overwrite` flag to remove an annotation from the Pod:

```bash
kubectl annotate pod my-pod my-annotation-key-2- # Note the trailing dash
```

2. Verify that the annotation has been removed from the Pod:

```bash
kubectl describe pod my-pod | grep my-annotation-key-2
```

You should not see the `my-annotation-key-2` annotation in the output.
