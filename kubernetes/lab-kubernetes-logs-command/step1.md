# Viewing Container Logs

In this step, you will learn how to view the logs of a container running in a pod.

1. Start by creating a deployment with one replica and an Nginx container:

   ```bash
   kubectl create deployment nginx --image=nginx --replicas=1
   ```

2. Wait for the pod to become ready:

   ```bash
   kubectl wait --for=condition=Ready pod -l app=nginx
   ```

3. Use the `kubectl logs` command to view the logs of the Nginx container:

   ```bash
   kubectl logs <pod_name>
   ```

Replace `<pod_name>` with the name of the pod created in step 1, and you can get the `<pod_name>` with the `kubectl get pod -l app=nginx` command.
