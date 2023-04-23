# Clean Up

In this step, we will clean up the resources we created in the previous steps.

1. Run the following command to stop and remove all running containers:

```bash
docker container stop $(docker container ls -aq)
docker container rm $(docker container ls -aq)
```

This command stops and removes all running containers.

2. Run the following command to remove the `my-web-server` image:

```bash
docker rmi my-web-server
```

This command removes the Docker image with the tag `my-web-server`.
