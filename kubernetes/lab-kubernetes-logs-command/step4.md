# Viewing Logs from Multiple Containers

In this step, you will learn how to view logs from multiple containers running in a pod.

1. Create a pod with two containers: Nginx and Fluentd:

   ```bash
   cat << EOF | kubectl apply -f -
   apiVersion: v1
   kind: Pod
   metadata:
     name: nginx-fluentd
   spec:
     containers:
     - name: nginx
       image: nginx
     - name: fluentd
       image: fluentd
   EOF
   ```

2. Wait for the pod to become ready:

   ```bash
   kubectl wait --for=condition=Ready pod nginx-fluentd
   ```

3. Use the `kubectl logs` command to view logs from both containers:

   ```bash
   kubectl logs nginx-fluentd -c nginx
   kubectl logs nginx-fluentd -c fluentd
   ```
