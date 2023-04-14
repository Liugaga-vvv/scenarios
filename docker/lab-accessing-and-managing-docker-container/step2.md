# Stopping a Container

In this step, we will stop a running container.

1. Run the following command to stop the container we started in the previous step:

```
docker stop my-container
```

This command stops the running container with the name `my-container`.

2. Run the following command to confirm that the container has been stopped:

```
docker ps -a
```

This command lists all containers, including stopped containers. You should see the `my-container` container in the list with a status of `Exited`.
