# Run a Job with Multiple Pods

In some cases, you may need to run a job with multiple pods for better performance. In this example, we will create a job that runs multiple pods to download files from a remote server.

Create a file named `multi-pod-job.yaml` in `/home/labex/project/` with the following contents:

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: download-job
spec:
  completions: 3
  parallelism: 2
  template:
    spec:
      containers:
        - name: downloader
          image: curlimages/curl
          command: ["curl", "-o", "/data/file", "http://example.com/file"]
          volumeMounts:
            - name: data-volume
              mountPath: /data
      restartPolicy: Never
      volumes:
        - name: data-volume
          emptyDir: {}
  backoffLimit: 4
```

In this file, we define a job named `download-job` that runs multiple pods with the `curlimages/curl` image. Each pod downloads a file from `http://example.com/file` and saves it to a shared volume named `data-volume`.

To create the job, run the following command:

```shell
kubectl apply -f multi-pod-job.yaml
```

You can check the status of the job by running the following command:

```shell
kubectl get jobs
```

Once the job is completed, you can view the logs of the pod by running the following command:

```shell
kubectl logs <POD_NAME>
```

Replace `<POD_NAME>` with the name of any pod that ran the job. You can see the download log of the file,and you can get the `<pod_name>` with the `kubectl get pod |grep download-job` command.

Congratulations, you have successfully run a job with multiple pods in Kubernetes!
