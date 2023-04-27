# Run a Cronjob

In addition to one-off jobs, Kubernetes also supports cronjobs for running tasks on a regular schedule. In this example, we will create a cronjob that runs a command every minute.

Create a file named `cronjob.yaml` in `/home/labex/project/` with the following contents:

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: hello-cronjob
spec:
  schedule: "*/1 * * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
            - name: hello
              image: busybox
              command: ["sh", "-c", 'echo "Hello, World!"']
          restartPolicy: Never
  successfulJobsHistoryLimit: 3
  failedJobsHistoryLimit: 3
```

In this file, we define a cronjob named `hello-cronjob` that runs a command every minute. The command is the same as the one we used in the first example to print "Hello, World!" to the console.

To create the cronjob, run the following command:

```shell
kubectl apply -f cronjob.yaml
```

You can check the status of the cronjob by running the following command:

```shell
kubectl get cronjobs
```

Once the cronjob is running, you can view the logs of the pod by running the following command:

```shell
kubectl logs -f <POD_NAME>
```

Replace `<POD_NAME>` with the name of any pod that was created by the cronjob,and you can get the `<pod_name>` with the `kubectl get pod |grep  hello-cronjob` command.

Congratulations, you have successfully run a cronjob in Kubernetes!
