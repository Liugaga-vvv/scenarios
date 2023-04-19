# Build A Docker Image

The next step is to use the Dockerfile to build a Docker image. To do this, follow these steps:

1. Run the following command to build the Docker image:

```bash
docker build -t myapp .
```

This command builds a Docker image called `myapp` using the Dockerfile in the current directory (`.`).

2. Run the following command to list all Docker images:

```bash
docker images
```

This command lists all Docker images on your host, including the `myapp` image you just built.
