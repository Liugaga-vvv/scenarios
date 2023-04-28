# Annotate a Pod With a Single Key-Value Pair

In this step, we will start with a simple example of annotating a Pod with a single key-value pair using the `kubectl annotate` command.

1. Create a file called `pod.yaml` in the `/home/labex/project` directory with the following content:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
    - name: nginx
      image: nginx
```

Create the Pod with the following command:

```bash
kubectl apply -f pod.yaml
```

2. Use the `kubectl annotate` command to add an annotation to the Pod:

```bash
kubectl annotate pod my-pod my-annotation-key=my-annotation-value
```

3. Verify that the annotation has been added to the Pod:

```bash
kubectl describe pod my-pod | grep Annotations
```

You should see the annotation `my-annotation-key` with the value `my-annotation-value` in the output.
