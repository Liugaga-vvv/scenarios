# Note

1. Input `kubectl taint nodes minikube node-role.kubernetes.io/control-plane:NoSchedule` command to taint a node.
2. Use `kubectl apply -f pod-not-tolerate.yaml` command to create a pod.
3. Use `kubectl describe pod pod-not-tolerate` command to get the pod information.
4. Use `kubectl apply -f pod-tolerate.yaml` command to create a pod.
5. Use `kubectl describe pod pod-tolerate` command to get the pod information.
