# Create a ClusterRole Binding

Create a ClusterRole Binding that binds the `myapp-admin` ClusterRole to a user or group in the cluster. For example, to bind the `myapp-admin` ClusterRole to the `cluster-admin` user, create the following YAML file called `myapp-admin-binding.yaml`:

```yaml
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: myapp-admin-binding
subjects:
  - kind: User
    name: cluster-admin
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: myapp-admin
  apiGroup: rbac.authorization.k8s.io
```

This ClusterRole Binding binds the `myapp-admin` ClusterRole to the `cluster-admin` user.

Create the ClusterRole Binding using the following command:

```shell
kubectl apply -f myapp-admin-binding.yaml
```
