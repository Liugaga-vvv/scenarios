# Following Logs in Real-Time

In this step, you will learn how to follow logs in real-time as they are generated.

1. Use the `kubectl logs` command with the `-f` option to follow logs in real-time:

   ```bash
   kubectl logs -f nginx-busybox
   ```

2. Open a new terminal and create a shell in the Nginx container:

   ```bash
   kubectl exec -it nginx-busybox -c nginx -- /bin/sh
   ```

3. Generate some logs by running a command inside the container:

   ```bash
   curl 127.0.0.1
   ```

4. Switch back to the first terminal where you are following the logs and observe that the new log entry is displayed.
