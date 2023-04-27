# Create a Role Binding

Create a Role Binding that binds the `myapp-reader` Role to a user or group in the `myapp` namespace. For example, to bind the `myapp-reader` Role to the `developer` user in the `myapp` namespace, create the following YAML file called `myapp-reader-binding.yaml`:

```yaml
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: myapp-reader-binding
  namespace: myapp
subjects:
  - kind: User
    name: developer
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: myapp-reader
  apiGroup: rbac.authorization.k8s.io
```

This Role Binding binds the `myapp-reader` Role to the `developer` user in the `myapp` namespace.

Create the Role Binding using the following command:

```shell
kubectl apply -f myapp-reader-binding.yaml
```
