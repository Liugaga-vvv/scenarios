# Test Access

Test access to the `myapp` namespace by attempting to get the list of pods in the namespace using the following command:

```shell
kubectl get pods -n myapp --as developer
```

You should see a message indicating that no resources in myapp namespace, because you might not have pods in your cluster.When you're done with the lab, use this command and you should see a list of pods in the `myapp` namespace.

Test access to the `default` namespace by attempting to get the list of pods in the namespace using the following command:

```shell
kubectl get pods --as developer
```

You should see an error message indicating that you do not have access to the `default` namespace.
