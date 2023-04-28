# Run a Pod with a Job

The first step is to create a pod that runs a job. In this example, we will create a pod that runs a command to print "Hello, World!" to the console.

Create a file named `job.yaml`in `/home/labex/project/` with the following contents:

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: hello-job
spec:
  template:
    spec:
      containers:
        - name: hello
          image: busybox
          command: ["sh", "-c", 'echo "Hello, World!"']
      restartPolicy: Never
  backoffLimit: 4
```

In this file, we define a job named `hello-job` that runs a single container named `hello`. The container runs the `busybox` image and executes a command to print "Hello, World!" to the console.

To create the job, run the following command:

```shell
kubectl apply -f job.yaml
```

You can check the status of the job by running the following command:

```shell
kubectl get jobs
```

Once the job is completed, you can view the logs of the pod by running the following command:

```shell
kubectl logs <POD_NAME>
```

Replace `<POD_NAME>` with the name of the pod that ran the job,and you can get the `<pod_name>` with the `kubectl get pods |grep  hello-job` command.

Congratulations, you have successfully run a pod with a job in Kubernetes!
