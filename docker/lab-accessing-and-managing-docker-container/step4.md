# Removing a Container

In this step, we will remove a container.

1. Run the following command to remove the container we started in the previous step:

```
docker rm my-shell-container
```

This command removes the container with the name `my-shell-container`.

2. Run the following command to confirm that the container has been removed:

```
docker ps -a
```

This command lists all containers, including stopped containers. You should not see the `my-shell-container` container in the list.
