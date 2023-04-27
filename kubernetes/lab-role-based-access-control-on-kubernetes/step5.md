# Create a ClusterRole

Create a new ClusterRole called `myapp-admin` that allows users to create, delete, and update pods and services in all namespaces using the following YAML file called `myapp-admin-clusterrole.yaml`:

```yaml
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: myapp-admin
rules:
  - apiGroups: [""]
    resources: ["pods", "services"]
    verbs: ["get", "list", "watch", "create", "update", "delete"]
```

This ClusterRole allows users to perform all operations (get, list, watch, create, update, and delete) on pods and services in all namespaces.

Create the ClusterRole using the following command:

```shell
kubectl apply -f myapp-admin-clusterrole.yaml
```
