# Manage Docker Containers

In this step, we will learn how to manage Docker containers.

1. Run the following command to see the list of running Docker containers:

```bash
docker ps
```

This command lists all the running Docker containers along with their status, container ID, image, and other information.

2. Run the following command to stop the container we started in the previous step:

```bash
docker stop <CONTAINER_ID>
```

Replace `<CONTAINER_ID>` with the ID of the container you want to stop. You can get the container ID from the output of the `docker ps` command.

3. Run the following command to remove the container:

```bash
docker rm <CONTAINER_ID>
```

Replace `<CONTAINER_ID>` with the ID of the container you want to remove.
