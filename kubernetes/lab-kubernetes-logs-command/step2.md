# Viewing Logs from a Specific Container in a Pod

In this step, you will learn how to view the logs of a specific container running in a pod.

1. Create a pod with two containers: Nginx and BusyBox:

   ```bash
   cat << EOF | kubectl apply -f -
   apiVersion: v1
   kind: Pod
   metadata:
     name: nginx-busybox
   spec:
     containers:
     - name: nginx
       image: nginx
     - name: busybox
       image: busybox
       command:
         - sleep
         - "3600"
   EOF
   ```

2. Wait for the pod to become ready:

   ```bash
   kubectl wait --for=condition=Ready pod nginx-busybox
   ```

3. Use the `kubectl logs` command to view the logs of the BusyBox container:

   ```bash
   kubectl logs nginx-busybox -c busybox
   ```
