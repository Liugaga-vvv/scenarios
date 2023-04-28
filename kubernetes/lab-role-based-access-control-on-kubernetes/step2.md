# Create a Role

Create a new Role called `myapp-reader` in the `myapp` namespace that allows users to read pods and services in the namespace using the following YAML file called `myapp-reader-role.yaml`:

```yaml
kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  namespace: myapp
  name: myapp-reader
rules:
  - apiGroups: [""]
    resources: ["pods", "services"]
    verbs: ["get", "watch", "list"]
```

This Role allows users to read (get, watch, and list) pods and services in the `myapp` namespace.

Create the Role using the following command:

```shell
kubectl apply -f myapp-reader-role.yaml
```
