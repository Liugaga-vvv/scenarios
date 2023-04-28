# Create a Namespace

In this step, you will create a namespace called `webapp` to isolate the web application from the other resources in the cluster.

Create a file called `namespace.yaml` with the following contents:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: webapp
```

Apply the namespace to your cluster with the following command:

```shell
kubectl apply -f namespace.yaml
```

Verify that the namespace was created with the following command:

```shell
kubectl get namespaces
```

You should see the `webapp` namespace in the list of namespaces.
